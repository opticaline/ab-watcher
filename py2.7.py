# -*- coding: utf-8 -*-


def run():
    import logging.config
    # 使用配置文件配置logging
    logging.config.fileConfig("config/logger.conf")

    from utils import main

    result = main.flashlight_plugin_result('恩率')
    main.play_video(result.get('run_args')[0])


if __name__ == '__main__':
    run()
