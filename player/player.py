# -*- coding: utf-8 -*-
from utils import config

class BasePlayer:
    config = config

    def __init__(self, cmd=None):
        if cmd is None:
            self.cmd = self.config.get_property('{platform}.player-cmd')
        else:
            self.cmd = cmd
