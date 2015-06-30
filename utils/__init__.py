# -*- coding: utf-8 -*-
import os
from .requests import Requests
from .config import Configuration

config = Configuration(__path__[0] + '{0}..{0}config'.format(os.path.sep))

http = config.get_property('http-proxy')
if http is not None:
    Requests.set_proxy(http=http)

__all__ = ['config']
