# -*- coding: utf-8 -*-

from utils import main
import logging.config

logging.config.fileConfig("config/logger.conf")


def results(fields, original_query):
    message = fields['~message'].encode('utf8')
    return main.flashlight_plugin_result(message)


def run(message):
    main.play_video(message)
