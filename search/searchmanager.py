# -*- coding: utf-8 -*-

import re
from .search import AcFunSearch, BiliBiliSearch
from utils.common import DictUtils

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
        self.all_type.add(DefaultArgs.get('HISTORY'))

        if re.match('^,*\d*$', args[-1]):
            length = len(args[-1])
            args[-1] = args[-1].replace(',', '')
            self.page_num = length - len(args[-1]) + 1
            if args[-1] is not None and args[-1] != '':
                self.index = int(args[-1]) - 1
            args = args[:-1]
        self.args = args

    def parser(self):
        scope, style, search_word = None, None, None
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
                search_word = self.args[0]
        else:
            scope = self.args[0]
            style = DefaultArgs.get('SEARCH')
            search_word = ' '.join(self.args[1:])
        return DictUtils({
            'scope': scope,
            'style': style,
            'search_word': search_word,
            'page_num': self.page_num,
            'index': self.index
        })


class SearchManager:
    options = {}
    source = None
    searcher = []

    def __init__(self, options=None, source=None):
        if not options:
            options = {}
        self.options = options
        self.source = source
        if self.options.GetAcFun:
            self.searcher.append(AcFunSearch(self.source['AcFun']))
        if self.options.GetBilibili:
            self.searcher.append(BiliBiliSearch(self.source['BiliBili']))

    def search(self, kwargs):
        if kwargs.scope == DefaultArgs.get('HELP'):
            return []
        elif kwargs.scope == DefaultArgs.get('HISTORY'):
            from utils import history

            return history.get_all()
        else:
            return self.get_data(kwargs)

    def get_data(self, kwargs):
        data = []
        for searcher in self.searcher:
            data += searcher.search(kwargs)
        return data
