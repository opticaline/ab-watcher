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

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def request(self):
        opener = urllib2.build_opener(Requests.proxy)
        urllib2.install_opener(opener)
        return urllib2.urlopen(self.url).read()

    @staticmethod
    def get_json(**kwargs):
        try:
            return json.loads(Requests(**kwargs).request())
        except ValueError, err:
            logger.warning('{1}, on loading url: {0}'.format(kwargs['url'], err))
            return None

    @staticmethod
    def get_soup(**kwargs):
        html = Requests(**kwargs).request()
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
