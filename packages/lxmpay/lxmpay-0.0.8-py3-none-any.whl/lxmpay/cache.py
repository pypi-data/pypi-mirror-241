import time


class Cache(object):
    async def get(self, key, default=None):
        raise NotImplementedError()

    async def set(self, key, value, ttl=None):
        raise NotImplementedError()

    async def delete(self, key):
        raise NotImplementedError()


class MemoryCache(Cache):
    def __init__(self):
        self._cache = {}

    async def set(self, key, value, expire=0):
        self._cache[key] = (value, time.time() + expire if expire > 0 else 0)

    async def get(self, key):
        value, expire = self._cache.get(key) or (None, 0)
        if value and expire > 0 and expire < time.time():
            self._cache.pop(key)
            return None
        return value

    async def delete(self, key):
        self._cache.pop(key, None)


class RedisCache(Cache):
    def __init__(self, redis, prefix=""):
        self.redis = redis
        self.prefix = prefix

    def key_name(self, key):
        return "{0}:{1}".format(self.prefix, key)

    async def get(self, key, default=None):
        key = self.key_name(key)
        value = await self.redis.get(key)
        if value is None:
            return default

    async def set(self, key, value, ttl=None):
        if value is None:
            return
        key = self.key_name(key)
        self.redis.set(key, value, ex=ttl)

    async def delete(self, key):
        key = self.key_name(key)
        self.redis.delete(key)
