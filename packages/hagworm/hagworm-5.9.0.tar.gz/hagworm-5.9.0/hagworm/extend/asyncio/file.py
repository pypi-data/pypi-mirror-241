# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import typing

from ..cache import StackCache
from ..error import catch_error

from .net import HTTPClientPool, HttpType
from .future import ThreadPool


class FileLoader:
    """带缓存的网络文件加载器
    """

    def __init__(self, maxsize: int = 0xff, ttl: int = 3600, thread: int = 32):

        self._cache: StackCache = StackCache(maxsize, ttl)

        self._thread_pool: ThreadPool = ThreadPool(thread)
        self._http_client: HTTPClientPool = HTTPClientPool(limit=thread)

    @staticmethod
    def _read(file: str) -> typing.AnyStr:

        with open(file, r'rb') as stream:
            return stream.read()

    async def read(self, file: str) -> typing.AnyStr:

        result = None

        with catch_error():

            if self._cache.has(file):

                result = self._cache.get(file)

            else:

                result = await self._thread_pool.run(self._read, file)

                self._cache.set(file, result)

        return result

    async def fetch(
            self, url: str, params: typing.Optional[HttpType.QueryParamTypes] = None, *,
            cookies: typing.Optional[HttpType.CookieTypes] = None,
            headers: typing.Optional[HttpType.HeaderTypes] = None
    ) -> typing.AnyStr:

        result = None

        with catch_error():

            if self._cache.has(url):

                result = self._cache.get(url)

            else:

                result = await self._http_client.get(url, params=params, cookies=cookies, headers=headers)

                self._cache.set(url, result)

        return result
