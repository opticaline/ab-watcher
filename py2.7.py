# -*- coding: utf-8 -*-
import logging.config

if __name__ == '__main__':
    # 使用配置文件配置logging
    logging.config.fileConfig("config/logger.conf")
    logger = logging.getLogger('utils')

    from utils import main

    infos = main.video_list(['qyqx'])
    main.play_video(infos[0])
