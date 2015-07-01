# -*- coding: utf-8 -*-
import logging

import sys
from optparse import OptionParser
from analysis.analysis import Analysis
from player import Player
from utils import config


def make_args(args):
    parser = OptionParser()
    parser.add_option("-a", "--acfun", action="store_false", dest="GetAcFun", default=True,
                      help="Get movies from AcFun.tv")
    parser.add_option("-b", "--bilibili", action="store_false", dest="GetBilibili", default=True,
                      help="Get movies from BiliBili.tv")
    parser.add_option("-c", "--cache", action="store_true", dest="UseCache", default=False,
                      help="Cache the website result")
    parser.add_option("-s", "--source", dest="Source", metavar="FILE", default="config/source.json",
                      help="write report to FILE")

    return parser.parse_args(config.get_properties('default-args') + args)


def video_list(args=None):
    if not args:
        args = sys.argv
    (options, args) = make_args(args)

    if len(args) > 0:
        from search import SearchManager

        manager = SearchManager(options)
        return manager.search(args)
    return []


def play_video(info):
    analysis = Analysis(info=info)
    video = analysis.get_video()
    logger = logging.getLogger(__name__)
    logger.debug(video)
    video = ['D:/videos/0300022F0051C4A0375C73092DCCF72F96DB86-FAFC-CBE5-8A3D-F5DC188425DB.flv']
    subtitle = analysis.get_ass_path()
    Player().play(video, subtitle, info['title'])
