from redis.asyncio import from_url
from functools import wraps

connect_redis = from_url('redis://127.0.0.1:6379')


async def key_builder(func, *args, **kwargs) -> str:
    return f"{func.__module__}-{func.__name__}-{args}-{kwargs}"


def cache(expire:int):

    def wrapper(func):

        @wraps(func)
        async def inner(*args, **kwargs):

            cache_key = await key_builder(func, *args, **kwargs)

            cached = await connect_redis.get(cache_key)
            if cached:
                return cached

            result = await func(*args, **kwargs)
            await connect_redis.set(cache_key, str(result), ex=expire)

            return result

        return inner

    return wrapper

