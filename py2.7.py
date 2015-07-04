# -*- coding: utf-8 -*-


def run():
    import logging.config
    # 使用配置文件配置logging
    logging.config.fileConfig("config/logger.conf")

    # from utils import common
    #
    # print(common.format('12{he[keyword]llo}34\{pass\}56{keyword}7890', {'keyword': ' wow '}))

    from utils import main

    infos = main.flashlight_plugin_result('恩率')
    # infos = main.flashlight_plugin_result('movie 恩率')
    # infos = main.flashlight_plugin_result('movie 恩率 ,')
    infos = main.flashlight_plugin_result('movie 恩率 ,3')
    print(infos)

    # html = Requests('http://search.acfun.tv/search?cd=1&type=2&q=%E7%96%AF%E7%8B%82%E7%9A%84&sortType=-1&field=title&sortField=score&pageNo=1&pageSize=10&aiCount=3&spCount=3&isWeb=1&sys_name=pc').request()
    # html = Requests('http://static.comment.acfun.mm111.net/2266943-0').request()
    # print(html)

if __name__ == '__main__':
    run()
