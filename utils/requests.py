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

    def __init__(self, url, **kwargs):
        self.__dict__ = kwargs
        self.url = url

    def request(self):
        if Requests.proxy is not None:
            opener = urllib2.build_opener(Requests.proxy)
            urllib2.install_opener(opener)
        request = urllib2.urlopen(self.url)
        temp = request.info().get('Content-Type')
        if temp is not None:
            temp = temp.split('charset=')
            if len(temp) == 2:
                self.encoding = temp[1]
        # print(self.encoding)
        return request.read()

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
    def quote(s, safe='/'):
        return urllib2.quote(s, safe)