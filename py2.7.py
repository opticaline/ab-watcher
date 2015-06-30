# -*- coding: utf-8 -*-
import logging.config

if __name__ == '__main__':
    # 使用配置文件配置logging
    logging.config.fileConfig("config/logger.conf")

    # from utils import common
    #
    # print(common.format('12{he[keyword]llo}34\{pass\}56{keyword}7890', {'keyword': ' wow '}))

    from utils import main

    print(main.video_list(['qyqx']))
