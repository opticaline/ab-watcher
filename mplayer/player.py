# -*- coding: utf-8 -*-
__author__ = 'opticaline'

from mplayer.mpv import Mpv
from subprocess import Popen


class BasePlayer:
    mplayer_path = None
    _mp = None
    args = None

    def __init__(self, mplayer_path, args):
        self.mplayer_path = mplayer_path
        self.args = args
        self._mplayer()

    def _mplayer(self):
        cmd = [self.mplayer_path, '-slave', '-quiet', '-idle']
        cmd.extend(self.args)
        cmd += ['D:\Test.wmv', '-ass', '-sub', 'D:\QYQX.ass']
        print(cmd)
        self._mp = Popen(cmd)

    def test(self):
        return self._mp

Player = Mpv

