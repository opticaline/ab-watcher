# -*- coding: utf-8 -*-
from subprocess import Popen

__author__ = 'opticaline'


class Mpv:
    mpv_path = None
    mpv = None

    def __init__(self, mpv_path='D:/mpv/mpv.exe'):
        self.mpv_path = mpv_path

    def play(self, file_list, subtitle, title=None):
        cmd = [self.mpv_path, '--volume', '20', '--merge-files']
        cmd.extend(file_list)
        # subtitle
        if subtitle is not None:
            cmd.extend(['--sub-file', subtitle])
        if title is not None:
            cmd.extend(['--title', title])
        print(' '.join(cmd))
        self.mpv = Popen(cmd)
