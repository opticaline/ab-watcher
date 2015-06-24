# -*- coding: utf-8 -*-
import json
from search.search import AcFunSearch


class ArgsParser:
    all_type = set()

    def __init__(self, args, source):
        self.args = args
        for site in source:
            for t in source[site]:
                self.all_type.add(t)

    def parser(self):
        t, key, scope = None, None, None
        if len(self.args) == 0:
            t = 'hot'
        elif len(self.args) == 1:
            if self.args[0] in self.all_type:
                t = self.args[0]
            else:
                t = 'search'
                key = self.args[0]
        elif len(self.args) == 2:
            t = 'search'
            scope = self.args[0]
            key = self.args[1]
        else:
            pass
        return t, key, scope


class SearchManager:
    options = {}
    source = None
    searcher = []

    def __init__(self, options=None):
        if not options:
            options = {}
        self.options = options
        self.source = json.loads(open(self.options.Source).read())
        if self.options.GetAcFun:
            self.searcher.append(AcFunSearch(self.source['AcFun']))
        if self.options.GetBilibili:
            self.searcher.append(AcFunSearch(self.source['BiliBili']))

    def search(self, args):
        t, k, s = ArgsParser(args, self.source).parser()
        if t is not None:
            return self.get_data(t, {'keyword': k, 'scope': s} if k is not None else None)
        else:
            return []

    def get_data(self, t, keyword=None):
        print(t)
        print(keyword)
        data = []
        for searcher in self.searcher:
            data += searcher.search(t, keyword)
        return data
