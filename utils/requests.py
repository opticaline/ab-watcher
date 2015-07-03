# -*- coding: utf-8 -*-
import json
import urllib2
import logging

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Requests:
    url = None
    params = None
    method = None
    proxy = None
    encoding = None
    useCache = False
    cachePath = None

    def __init__(self, url, **kwargs):
        self.__dict__ = kwargs
        self.url = url

    def request(self):
        if self.useCache:
            cache = self.get_cache()
            if cache is not None:
                return cache
        if Requests.proxy is not None:
            opener = urllib2.build_opener(Requests.proxy)
            urllib2.install_opener(opener)
        request = urllib2.urlopen(self.url)
        temp = request.info().get('Content-Type')
        if temp is not None:
            temp = temp.split('charset=')
            if len(temp) == 2:
                self.encoding = temp[1]
        text = request.read()
        if Requests.useCache:
            self.set_cache(text)
        print(self.encoding)
        return text

    def get_cache(self):
        import os

        text = None
        path = self.get_cache_file()
        if os.path.exists(path):
            f = open(path, 'r')
            text = f.read()
            f.close()
        return text

    def set_cache(self, text):
        f = open(self.get_cache_file(), 'w')
        f.write(text)
        f.close()

    def get_cache_file(self):
        import hashlib, time

        return self.cachePath + hashlib.md5(self.url).hexdigest() + time.strftime("-%Y-%m-%d")

    def get_json(self):
        try:
            return json.loads(self.request())
        except ValueError, err:
            logger.warning('{1}, on loading url: {0}'.format(self.url, err))
            return None

    def get_soup(self):
        html = self.request()
        return BeautifulSoup(html)

    @staticmethod
    def set_proxy(http=None, https=None):
        p = dict()
        if http is not None:
            p.setdefault('http', http)
        if https is not None:
            p.setdefault('https', https)
        if len(p.keys()) > 0:
            Requests.proxy = urllib2.ProxyHandler(p)

    @staticmethod
    def use_cache(path):
        Requests.useCache = True
        Requests.cachePath = path

    @staticmethod
    def quote(s, safe='/'):
        return urllib2.quote(s, safe)
