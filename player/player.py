# -*- coding: utf-8 -*-
from config import Config

__author__ = 'opticaline'


class BasePlayer:
    config = Config()

    def __init__(self, cmd=None):
        if cmd is None:
            self.cmd = self.config['player-cmd']
        else:
            self.cmd = cmd
