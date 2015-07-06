# -*- coding: utf-8 -*-
import json
import logging
import sys
from optparse import OptionParser

from analysis.analysis import Analysis
from player import Player
from search import SearchManager
from search.searchmanager import ArgsParser
from utils import config
from utils import history


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
        source = json.loads(open(options.Source).read())
        kwargs = ArgsParser(args, source).parser()
        manager = SearchManager(options, source)
        return manager.search(kwargs), kwargs.index
    return []


def play_video(info):
    history.add(info)
    analysis = Analysis(info=info)
    video = analysis.get_video()
    logger = logging.getLogger(__name__)
    logger.debug(video)
    subtitle = analysis.get_ass_path()
    Player().play(video, subtitle, info['title'])


def flashlight_plugin_result(message):
    out, index = video_list(message.split(' '))
    l = out
    if out is None or len(out) == 0:
        return None

    if index != 0:
        l = [out[index]]
    return {
        "title": "{0}".format(out[index]['title'].encode('utf-8')),
        "run_args": [out[index]],
        "html": '{0}'.format(make_template(l))
    }


def make_template(data):
    if len(data) == 1:
        # TODO 当只有一个匹配时显示布局发生变化
        return list_template(data)
    else:
        return list_template(data)


def list_template(l):
    f = open('resources/style.html', 'r')
    html = f.read()
    f.close()
    index = 1
    f = open('resources/list.html', 'r')
    template = f.read()
    f.close()
    for i in l:
        html += template.format(
            i['username'].encode('utf-8'),
            i['covers'],
            i['title'].encode('utf-8'),
            i['description'].encode('utf-8'),
            i['views'],
            index,
            i['logo'])
        index += 1
    return html
