import json
from org.opticaline.ab.search.search import *

__author__ = 'opticaline'


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
        return self.getdata(*args)

    def getdata(self, t, keyword=None):
        data = []
        for i in range(len(self.searcher)):
            data += self.searcher[i].search(t, keyword)
        return data
