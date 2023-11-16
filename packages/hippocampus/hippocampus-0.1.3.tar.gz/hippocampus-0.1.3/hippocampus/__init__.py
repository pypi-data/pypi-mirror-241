"""
Main file
"""
import functools
import inspect
import pathlib
import datetime

import dateparser
import orjson
from pip._internal.utils.appdirs import user_cache_dir

from peewee import *
from playhouse.sqlite_ext import *

db = None


def setup_db(db_path=None):
    cache_dir = pathlib.Path(user_cache_dir('hippocampus'))
    cache_dir.mkdir(exist_ok=True, parents=True)

    db_path = db_path or (cache_dir / 'db.sqlite3')
    global db
    db = SqliteDatabase(db_path,
                        pragmas={'journal_mode': 'wal',
                                 'cache_size': -1024 * 1000})
    with db.bind_ctx([MemoizedCall]):
        MemoizedCall.create_table(True)
    return db


class MemoizedCall(Model):
    fn_name = CharField()
    arguments = JSONField(json_dumps=orjson.dumps, json_loads=orjson.loads)
    result = JSONField(json_dumps=orjson.dumps, json_loads=orjson.loads)

    created = DateTimeField(default=datetime.datetime.utcnow, index=True)
    expires = DateTimeField(index=True, null=True)

    class Meta:
        indexes = (
            # unique together
            (('fn_name', 'arguments'), True),
        )


def calculate_expiry(remember):
    if remember.lower() == "forever":
        return None
    else:
        return dateparser.parse(remember,
                                settings={
                                    'TIMEZONE': 'UTC',
                                    'PREFER_DATES_FROM': 'future',
                                })


def write_cache(fn, call_args, expires):
    result = fn(**call_args)
    MemoizedCall.insert(
        fn_name=fn.__name__,
        arguments=call_args,
        result=result,
        expires=expires,
    ).on_conflict_ignore().execute()
    return result


def read_cache(fn, call_args, expires):
    if expires:
        result = (MemoizedCall
                  .select()
                  .where(MemoizedCall.fn_name == fn.__name__,
                         MemoizedCall.arguments == call_args,
                         MemoizedCall.expires >= datetime.datetime.utcnow())
                  )
    else:
        result = (MemoizedCall
                  .select()
                  .where(MemoizedCall.fn_name == fn.__name__,
                         MemoizedCall.arguments == call_args)
                  )
    try:
        return result.get().result
    except MemoizedCall.DoesNotExist:
        return False


def memoize(remember="forever",
            overwrite=False,
            db_path=None):
    """
    Memoizing decorator
    todo: cache generators?
    """
    def decorator(fn):
        # Code smell, should get rid of global var
        global db
        db = db or setup_db(db_path)

        @functools.wraps(fn)
        def inner(*args, **kwargs):
            call_args = inspect.getcallargs(fn, *args, **kwargs)
            with db.bind_ctx([MemoizedCall]):
                expires = calculate_expiry(remember)
                # Force write even if a cached result exists
                if overwrite:
                    result = write_cache(fn, call_args, expires)
                else:
                    result = read_cache(fn, call_args, expires) or write_cache(fn, call_args, expires)
                return result
        return inner
    return decorator
