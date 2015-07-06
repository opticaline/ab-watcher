# -*- coding: utf-8 -*-
import json
from utils import Requests, common


class Search:
    source = []

    def __init__(self, source):
        self.source = source

    def search(self, kwargs):
        pass
        # covers, url, title, description, views, username


class AcFunSearch(Search):
    def search(self, kwargs):
        result = []
        for url in self.source[kwargs.scope]:
            url = common.format(url, {
                'keyword': Requests.quote(kwargs.search_word),
                'page_num': str(kwargs.page_num)
            })
            result += self.translation(
                json.loads(Requests(url=url).request().replace('system.tv=', ''))['data']['page']['list'])
        return result

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
    def search(self, kwargs):
        params = {'keyword': Requests.quote(kwargs.search_word),
                  'page_num': str(kwargs.page_num)}.copy()
        params.update(self.source['scope'][kwargs.scope])

        url = common.format(self.source['urls'][kwargs.style], params)
        soup = Requests(url).get_soup()
        return self.__search_page(soup)

    @staticmethod
    def __search_page(soup):
        result = []
        for i in soup.select('.l.sp-guid'):
            temp = {}
            temp.setdefault('covers', i.find_all('img')[0]['src'])
            temp.setdefault('url', i.select('div.r_sp a')[0]['href'])
            title = i.select('div.r_sp a')[0]
            title.select('.t span')[0].clear()
            temp.setdefault('title', title.text.strip())
            temp.setdefault('description', i.select('.intro')[0].text)
            temp.setdefault('views', i.select('.w_info .gk')[0].text)
            temp.setdefault('username', i.select('.w_info .up a')[0].text)
            result.append(temp)
        return result
