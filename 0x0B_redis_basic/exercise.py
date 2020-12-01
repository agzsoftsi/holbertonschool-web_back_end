#!/usr/bin/env python3
""" Add Task 0 -  Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """A redis cache class
    Args:  _redis: private instance of the Redis client
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data in Redis using a random key
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        """Gets the value of a string and returns it converted to
        the right type
        """
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)
