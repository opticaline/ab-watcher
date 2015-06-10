__author__ = 'opticaline'

# mplayer.exe -sub ../Community.S06E08.720p.WEBRip.x264-BATV.简体.ass -subcp utf-8 http://localhost:63342/AB/Wildlife.wmv

class Ass:
    attr = dict()
    attr_name = ('Script Info', 'v4 Styles', 'Events', 'Fonts', 'Graphics', '', '', '', '')

    def __init__(self):
        pass

    def __str__(self):
        text = ''
        for name in self.attr:
            text += '[' + name + ']\n'
        return 'test'
