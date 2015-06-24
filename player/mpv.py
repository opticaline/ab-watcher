# -*- coding: utf-8 -*-
import logging
from subprocess import Popen
from player.player import BasePlayer

logger = logging.getLogger('ab')


class Mpv(BasePlayer):
    mpv = None
    volume = 20

    def __init__(self, mpv_path='D:/mpv/mpv.exe'):
        super().__init__(mpv_path)

    def set_volume(self, volume):
        self.volume = volume

    def play(self, file_list, subtitle, title=None):
        cmd = [self.cmd, '--volume', str(self.volume), '--merge-files']
        cmd.extend(file_list)
        # subtitle
        if subtitle is not None:
            cmd.extend(['--sub-file', subtitle])
        if title is not None:
            cmd.extend(['--title', title])
        logger.debug('Command run: {0}'.format(' '.join(cmd)))
        self.mpv = Popen(cmd)
