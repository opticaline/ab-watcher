# -*- coding: utf-8 -*-
import json
import os


class History:
    data_file_path = None

    def __init__(self, path):
        self.data_file_path = path
        if not os.path.exists(self.data_file_path):
            self.__save([])

    def add(self, message):
        message = json.dumps(message) + '\n'
        lines = [message] + self.__read()[:9]
        self.__save(lines)

    def __save(self, lines):
        f = open(self.data_file_path, 'w')
        f.write(''.join(lines))
        f.close()

    def __read(self):
        f = open(self.data_file_path, 'r')
        text = f.readlines()
        f.close()
        return text

    def get_all(self):
        temp = []
        for i in self.__read():
            temp.append(json.loads(i))
        return temp
