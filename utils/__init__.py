# -*- coding: utf-8 -*-
from .requests import Requests
from .config import Configuration

config = Configuration(__path__[0] + '\\..\\config')

Requests.set_proxy(http=config.get_property('http-proxy'))

__all__ = ['config']
