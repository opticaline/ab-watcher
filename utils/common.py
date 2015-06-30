# -*- coding: utf-8 -*-

import re


def format(s, params):
    return StringUtil(s).format(params)


class StringUtil:
    string = None

    def __init__(self, string):
        self.string = string

    def format(self, params):
        def repl(match):
            temp = match.groups()[0]
            if '[' in temp:
                temp = re.split('[\\[|\\]]', temp)
                temp[1] = params.get(temp[1])
                if temp[1] is None:
                    return ""
                else:
                    return "".join(temp)
            else:
                return params.get(match.groups()[0])

        return re.sub('(?<!\\\\){(.+?[^\\\\])}', repl, self.string)
