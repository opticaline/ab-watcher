# -*- coding: utf-8 -*-
from .requests import Requests
from .config import Configuration

config = Configuration(__path__[0] + '\\..\\config')

http = config.get_property('http-proxy')
if http is not None:
    Requests.set_proxy(http=http)

__all__ = ['config']
