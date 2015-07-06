# -*- coding: utf-8 -*-
import logging
from subprocess import Popen, PIPE
from utils import config

logger = logging.getLogger('player')


class BasePlayer:
    process = None
    config = config

    def __init__(self, cmd=None):
        if cmd is None:
            self.cmd = self.config.get_property('{platform}.player-cmd')
        else:
            self.cmd = cmd

    def run(self, cmd):
        self.process = Popen(cmd, stderr=PIPE, stdout=PIPE)

        if self.process.wait() != 0:
            logger.info(self.process.stdout.read())
            self.process.stdout.close()
            logger.error(self.process.stderr.read())
            self.process.stderr.close()
