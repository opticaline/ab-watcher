# -*- coding: utf-8 -*-
import json
import re
from .search import AcFunSearch, BiliBiliSearch

DefaultArgs = {
    'ALL': 'all',
    'HELP': 'help',
    'HISTORY': 'history',
    'HOT': 'hot',
    'SEARCH': 'search'
}


class ArgsParser:
    all_type = set()
    page_num = 1
    index = 0

    def __init__(self, args, source):
        for site in source:
            for t in source[site]:
                self.all_type.add(t)
        self.all_type.add(DefaultArgs.get('HELP'))

        if re.match('^,*\d*$', args[-1]):
            length = len(args[-1])
            args[-1] = args[-1].replace(',', '')
            self.page_num = length - len(args[-1]) + 1
            if args[-1] is not None and args[-1] != '':
                self.index = int(args[-1]) - 1
            args = args[:-1]
        self.args = args

    def parser(self):
        scope, style, searchword = None, None, None
        length = len(self.args)
        if length == 0:
            scope = DefaultArgs.get('HISTORY')
            style = DefaultArgs.get('HOT')
        elif length == 1:
            if self.args[0] in self.all_type:
                scope = self.args[0]
                style = DefaultArgs.get('HOT')
            else:
                scope = DefaultArgs.get('ALL')
                style = DefaultArgs.get('SEARCH')
                searchword = self.args[0]
        else:
            scope = self.args[0]
            style = DefaultArgs.get('SEARCH')
            searchword = ' '.join(self.args[1:])
        return scope, style, searchword, self.page_num, self.index


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
            self.searcher.append(BiliBiliSearch(self.source['BiliBili']))

    def search(self, args):
        scope, style, searchword, page_num, index = ArgsParser(args, self.source).parser()
        if scope == DefaultArgs.get('HELP'):
            return []
        elif scope == DefaultArgs.get('HISTORY'):
            return []
        else:
            return self.get_data(scope, style, searchword, page_num), index

    def get_data(self, scope, style, searchword, page_num):
        data = []
        for searcher in self.searcher:
            data += searcher.search(scope, style, searchword, page_num)
        return data
