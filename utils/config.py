# -*- coding: utf-8 -*-

__author__ = 'opticaline'

import os


class Configuration:
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
            print file_path

    def load_dir(self, file_path):
        for root, dirs, files in os.walk(file_path):
            for f in files:
                self.load_file(root + os.path.sep + f)
