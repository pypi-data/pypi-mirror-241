# Hippocampus

**working memory for your python code**

Hippocampus is a small library that persists function calls in a sqlite3 database.
It can be used through a(parameterized) decorator which caches calls and results.

### Usage

```python
from hippocampus import memoize


@memoize(remember="forever", db_path="mydb.sqlite3")
def my_expensive_function(arg, kwarg):
    pass

# first call is a regular function call
result = my_expensive_function("arg", kwarg={"a": "dict"})

# second call is a cached read from db
result = my_expensive_function("arg", kwarg={"a": "dict"})
```

### Parameters

`memoize()` takes three parameters:

- remember: How long to cache the result
- db_path: Set path for the database file. If not set, the user's cache directry (same as for pip) is used
- overwrite: Debug option to force overwriting existing records. May be useful if your code changed.

There is one (required) parameter `remember` which is used to set expiry of cached
items. The default is to not expire (keep forever). Other values may be given in
human readable terms and are parsed by `dateparser`. This means you can use either
absolute (`remember="2023-12-01"`) or relative (`remember="two minutes"`) date
specifications.
Note that the parameter means you will **need** to include parens on the decorator
even if you omit `remember`: Always use `@memoize()`.

### Limitations

The decorator is intentionally simple to remove complexity and **only accepts functions
with json-compatible args and outputs**. You can use any json-compatible type for
arguments and keyword arguments, but the return value needs to be a json-compatible
dictionary. In addition to the regular allowed types (str, int, list, dict), you can also
provide date/time objects, which will be serizalized and deserialized by the orjson
library.

Only straight return calls are supported; you cannot memoize a generator. This may
change in the future, but requires some db modeling considerations.

Finally, values are currently never deleted, even if they expire. Your memoization
database may thus grow to be rather large. Expired calls are overwritten when invoked
again, thus calling your memoized function after the expiry (even with a different expiry
setting) refreshes the old record.