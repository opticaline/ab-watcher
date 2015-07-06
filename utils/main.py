# -*- coding: utf-8 -*-
import logging

import sys
from optparse import OptionParser
from analysis.analysis import Analysis
from player import Player
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
        from search import SearchManager

        manager = SearchManager(options)
        return manager.search(args)
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
        "html": '{0}'.format(list_template(l))
    }

def list_template(l):
    html = ''
    index = 1
    template = '''<div style="border: 1px solid black; padding: 3px;margin-bottom: 1px;">
    <b style="display: block;">
        <i style="color: red; border-radius: 50%; background-color: black;padding: 0 5px;">
            {5}
        </i>
        {2}
    </b>
    <div style="display:table;clear:both;font-size:12px">
        <img style="width: 140px;height: 80px;float:left;margin-right:5px;" src="{1}">
        <span style="color: lightseagreen">
        {0}</span> ／ 播放:{4}<br>{3}
    </div>
</div>'''
    for i in l:
        html += template.format(
            i['username'].encode('utf-8'),
            i['covers'],
            i['title'].encode('utf-8'),
            i['description'].encode('utf-8'),
            i['views'],
            index)
        index += 1
    return html
