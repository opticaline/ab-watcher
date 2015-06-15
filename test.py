__author__ = 'Xu'

from subprocess import Popen

if __name__ == '__main__':
    p = Popen('mplayer')
    print(dir(p))
