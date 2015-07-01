# -*- coding: utf-8 -*-
import json
from utils import Requests
import re


class Search:
    source = []

    def __init__(self, source):
        self.source = source

    def search(self, t, keyword):
        pass
        # covers, url, title, description, views, username

    @staticmethod
    def get(url):
        return Requests(url=url).request()


class AcFunSearch(Search):
    def search(self, t, keyword):
        result = []
        for url in self.source[t]:
            url = self.set_params(url, keyword)
            if t == 'search':
                # TODO 增加对不同类型scope的搜索解析
                result += self.translation(json.loads(self.get(url).replace('system.tv=', ''))['data']['page']['list'])
            else:
                result += self.translation(json.loads(self.get(url)))
        return result

    @staticmethod
    def set_params(url, keyword=None):
        if not keyword:
            keyword = {}

        def repl(matched):
            return Requests.quote(keyword.get(matched.group("key"), ''))

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
