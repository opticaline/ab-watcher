# -*- coding: utf-8 -*-
from player import Player
from analysis.analysis import Analysis
from optparse import OptionParser
from search import SearchManager

__author__ = 'opticaline'

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-a", "--acfun", action="store_false", dest="GetAcFun", default=True,
                      help="Get movies from AcFun.tv")
    parser.add_option("-b", "--bilibili", action="store_false", dest="GetBilibili", default=True,
                      help="Get movies from BiliBili.tv")
    parser.add_option("-c", "--cache", action="store_false", dest="Cache", default=0,
                      help="Cache the website result")
    parser.add_option("-s", "--source", dest="Source", metavar="FILE", default="config/source.json",
                      help="write report to FILE")
    (options, args) = parser.parse_args()
    if len(args) > 0:
        manager = SearchManager(options)
        array = manager.search(args)
        #
        info = array[0]
        analysis = Analysis(info=info)
        video = analysis.get_video()
        video = ['D:/videos/0300022F0051C4A0375C73092DCCF72F96DB86-FAFC-CBE5-8A3D-F5DC188425DB.flv']
        subtitle = analysis.get_ass_path()
        Player().play(video, subtitle, info['title'])