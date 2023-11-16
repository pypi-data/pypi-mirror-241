import asyncio
import functools
import time
from typing import Any, Callable, Dict, Tuple

F = Callable[..., Any]
T = Tuple[Any, ...]


def cached(ttl: int) -> Callable[[F], F]:
    def decorator(f: F) -> F:
        cache: Dict[T, Tuple[float, Any]] = {}

        @functools.wraps(f)
        def wrapper(*args: T, **kwargs: Dict[str, Any]) -> Any:
            k = args + tuple(sorted(kwargs.items()))
            t = time.time()
            if (v := cache.get(k)) and t - v[0] < ttl:
                return v[1]
            r = f(*args, **kwargs)
            cache[k] = (t, r)
            return r

        @functools.wraps(f)
        async def async_wrapper(*args: T, **kwargs: Dict[str, Any]) -> Any:
            k = args + tuple(sorted(kwargs.items()))
            t = time.time()
            if (v := cache.get(k)) and t - v[0] < ttl:
                return v[1]
            r = await f(*args, **kwargs)
            cache[k] = (t, r)
            return r

        return async_wrapper if asyncio.iscoroutinefunction(f) else wrapper

    return decorator
