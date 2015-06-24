# -*- coding: utf-8 -*-
import logging.config

__author__ = 'opticaline'
if __name__ == '__main__':
    # 使用配置文件配置logging
    logging.config.fileConfig("config/logger.conf")
    # from utils import Requests
    # Requests.set_proxy(http='http://zhang-xu-neu:Bronze3!@192.168.107.27:8080')
    # # print Requests(url='http://acfun.tv').request()
    # # print Requests.get_json(url='http://static.comment.acfun.mm111.net/93875-0')
    # print Requests.get_json(url='http://acfun.tv')

    from utils import Configuration

    config = Configuration('D:\\resources\\ab.bundle\\config')
    print(config.get_properties('os.nt.player-cmd[test]'))
