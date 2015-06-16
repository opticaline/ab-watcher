import json
import urllib
from urllib.request import Request
import re

__author__ = 'opticaline'


class Ajax:
    opener = None

    def __init__(self, use_proxy=True):
        if use_proxy:
            proxy_hand = urllib.request.ProxyHandler({"http": "http://zhang-xu-neu:Bronze3!@192.168.107.27:8080"})
            self.opener = urllib.request.build_opener(proxy_hand)
        else:
            self.opener = urllib.request.build_opener()

    def get(self, url):
        return self.opener.open(url).readall().decode()


class Search:
    source = []
    ajax = None

    def __init__(self, source):
        self.source = source
        self.ajax = Ajax()

    def search(self, t, keyword):
        pass
        # covers, url, title, description, views, username

    def get(self, url):
        return self.ajax.get(url)


class AcFunSearch(Search):
    def search(self, t, keyword):
        result = []
        for url in self.source[t]:
            url = self.set_params(url, keyword)
            if t == 'search':
                result += self.translation(json.loads(self.get(url).replace('system.tv=', ''))['data']['page']['list'])
            else:
                result += self.translation(json.loads(self.get(url)))
        return result

    @staticmethod
    def set_params(url, keyword=None):
        if not keyword:
            keyword = {}

        def repl(matched):
            return keyword.get(matched.group("key"), '')

        return re.sub('\{(?P<key>\w+)\}', repl, url)

    @staticmethod
    def translation(data):
        result = []
        for d in data:
            result.append({
                'covers': d['titleImg'],
                'url': d['url'] or 'http://www.acfun.tv/' +
                                   ('aa' if d['contentId'].startswith('aa') else 'v') + '/' + d['contentId'],
                'title': d['title'],
                'description': d['description'],
                'views': d['views'],
                'username': d['username']
            })
        return result


class BiliBiliSearch(Search):
    pass
