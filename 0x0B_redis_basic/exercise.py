#!/usr/bin/env python3
""" Add Task 0 -  Writing strings to Redis """
import redis
from uuid import uuid4
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
        key = str(uuid4())
        self._redis.set(key, data)
        return key
