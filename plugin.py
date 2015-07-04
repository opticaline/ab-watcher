# -*- coding: utf-8 -*-

from utils import main
import logging.config

logging.config.fileConfig("config/logger.conf")


def results(fields, original_query):
    message = fields['~message']
    out = main.video_list([message])
    html = ''
    index = 1
    template = '''<div>
    <div style="display:inline-block"><img style="width: 140px;" src="{1}"></div>
    <div style="display:inline-block;padding: 10px;width: 200px;">
        <i style="color: red; border-radius: 50%; background-color: black;width: 20px;display: inline-block;">
        {5}
        </i>{0} / {2} / 播放({4})
    </div>
    <div>{3}</div>
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
        "title": "Say '{0}'".format(message),
        "run_args": [out[0]],
        "html": '{0}'.format(html)
    }


def run(message):
    main.play_video(message)
