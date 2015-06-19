# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import os

__author__ = 'opticaline'


class Config:
    _config = None
    _xml = None
    root = None
    os_attrs = ['player-cmd', 'subtitle-savepath']

    def __init__(self, path=None):
        if path is None:
            path = __file__.replace('py', 'xml')
        tree = etree.parse(path)
        self.root = tree.getroot()
        self.__taken_os(self.root.find('os').find(os.name))
        # for i in self.root:
        #     print(i.keys)

    def __taken(self):
        for node in self.root:
            print(node)

    def __taken_os(self, node):
        for a in self.os_attrs:
            self.__dict__[a] = node.find(a).text

    def __getitem__(self, item):
        return self.__dict__[item]
