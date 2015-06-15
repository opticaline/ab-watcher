__author__ = 'opticaline'

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
        # cmd += ['/Users/Xu/Downloads/test.flv']
        print(cmd)
        self._mp = Popen(cmd)

    def test(self):
        return self._mp
