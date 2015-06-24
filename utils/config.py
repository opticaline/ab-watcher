# -*- coding: utf-8 -*-

import os
from xml.etree import ElementTree


class Configuration:
    trees = dict()
    current_nodes = None

    def __init__(self, file_path=None):
        if file_path is not None:
            self.load(file_path)

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

    def load_dir(self, file_path):
        for root, dirs, files in os.walk(file_path):
            for f in files:
                self.load_file(root + os.path.sep + f)

    def get_properties(self, key, setting=None):
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

    def __get_child(self, key):
        self.__all_do(lambda element: element.findall(key))

    def __get_text(self):
        self.__all_do(lambda element: [element.text])

    def __get_attr(self, name):
        self.__all_do(lambda element: [element.attrib.get(name, None)])

    def __all_do(self, fn):
        result = []
        for element in self.current_nodes:
            t = fn(element)
            if t is not None:
                result.extend(t)
        self.current_nodes = result
