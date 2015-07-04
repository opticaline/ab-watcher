# -*- coding: utf-8 -*-

from utils import main
import logging.config

logging.config.fileConfig("config/logger.conf")


def results(fields, original_query):
    message = fields['~message'].encode('utf8')
    out = main.video_list([message])
    if out is None:
        return None
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
    for i in out:
        html += template.format(
            i['username'].encode('utf-8'),
            i['covers'],
            i['title'].encode('utf-8'),
            i['description'].encode('utf-8'),
            i['views'],
            index)
        index += 1
    return {
        "title": "{0}".format(out[0]['title'].encode('utf-8')),
        "run_args": [out[0]],
        "html": '{0}'.format(html)
    }


def run(message):
    main.play_video(message)
