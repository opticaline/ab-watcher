# -*- coding: utf-8 -*-
import os
import logging
from xml.etree import ElementTree
import sys
from utils import common

logger = logging.getLogger(__name__)


class Configuration:
    trees = dict()
    current_nodes = None

    keywords = dict()

    def __init__(self, file_path=None):
        if file_path is not None:
            self.load(os.path.realpath(file_path))
        self.__init_keywords()

    def __init_keywords(self):
        self.keywords.setdefault('platform', sys.platform)
        logger.info('config keywords {0}'.format(self.keywords))

    def load(self, file_path):
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                self.load_file(file_path)
            elif os.path.isdir(file_path):
                self.load_dir(file_path)

    def load_file(self, file_path):
        if file_path.endswith('xml'):
            tree = ElementTree.parse(file_path)
            name = os.path.basename(file_path).replace('.xml', '')
            self.trees.setdefault(name, tree)
            logger.info('Loading xml \'{}\''.format(file_path))

    def load_dir(self, file_path):
        logger.info('Loading folder \'{}\''.format(file_path))
        for root, dirs, files in os.walk(file_path):
            for f in files:
                self.load_file(root + os.path.sep + f)

    def get_property(self, key, setting=None):
        temp = self.get_properties(key, setting)
        return temp[0] if len(temp) > 0 else None

    def get_properties(self, key, setting=None):
        key = self.pretreatment(key)
        self.current_nodes = []
        if setting is not None:
            temp = self.trees.get(setting)
            if temp is not None:
                self.current_nodes.append(temp)
            else:
                return []
        else:
            for tree in self.trees.values():
                self.current_nodes += tree.findall('.')

        name = ''
        for i in key:
            if i == '.' or i == '[':
                self.__get_child(name)
                name = ''
            elif i == ']':
                self.__get_attr(name)
                return self.current_nodes
            else:
                name += i

        self.__get_child(name)
        self.__get_text()
        return self.current_nodes

    def pretreatment(self, key):
        return common.format(key, self.keywords)

    def __get_child(self, key):
        self.__all_do(lambda element: element.findall(key))

    def __get_text(self):
        self.__all_do(lambda element: [element.text])

    def __get_attr(self, name):
        def fn(element):
            t = element.attrib.get(name, None)
            if t is not None:
                return [t]
            return []

        self.__all_do(fn)

    def __all_do(self, fn):
        result = []
        for element in self.current_nodes:
            t = fn(element)
            if t is not None:
                result.extend(t)
        self.current_nodes = result
