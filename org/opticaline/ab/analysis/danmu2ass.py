__author__ = 'opticaline'


class DanMuManager:
    handler_map = dict()

    def __init__(self):
        self.handler_map['acfuc'] = AcFun2Ass

    def can_do(self, site):
        return site in self.handler_map.keys()

    def trans(self, site, url):
        handler = self.handler_map[site]
        return handler(url).trans()


class DanMu2Ass:
    def trans(self):
        pass


class AcFun2Ass(DanMu2Ass):
    pass
