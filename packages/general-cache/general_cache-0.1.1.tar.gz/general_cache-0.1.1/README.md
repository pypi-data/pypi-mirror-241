```
from general_cache import cached

@cached(10)
def f():
    ...

@cached(10)
async def g():
    ...
```
