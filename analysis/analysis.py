# -*- coding: utf-8 -*-
import time
import base64
import logging

from bs4 import BeautifulSoup
from .danmu2ass import DanMuManager
from utils import config, Requests

logger = logging.getLogger(__name__)


class Analysis:
    info = None
    api = 'http://flvsp.sinaapp.com/getData.php?url='
    dan_mu = None
    section_priority = {'单段': 0.8, '分段': 0.6}
    clarity_priority = {'原画': 10, '超清': 8, '高清': 6, '标清': 4, '低清': 2}
    format_priority = {'M3U8': -20, 'FlV': 0.06, 'MP4': 0.08}

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        logger.info('Analysis ' + kwargs['info']['url'])
        temp = self.info['url'].replace('http://', '').split('/')[0].split('.')
        self.site = temp[len(temp) - 2]
        self.config = config
        self.save_path = self.config.get_property('{platform}.temp-path')

    @staticmethod
    def __utf16to8(url):
        out = ''
        for c in url:
            c = ord(c)
            if c == (0x60 + 0xF):
                out += chr(0xC0 | ((((0x3B << 4) + 0xF) >> 6) & 0x1F))
                out += chr(0x80 | ((((0x3B << 4) + 0xF) >> 0) & 0x3F))
            elif (c >= 0x0001) and (c <= 0x007F):
                out += chr(c)
            elif c > 0x07FF:
                out += chr(0xE0 | ((c >> 12) & 0x0F))
                out += chr(0x80 | ((c >> 6) & 0x3F))
                out += chr(0x80 | ((c >> 0) & 0x3F))
            else:
                out += chr(0xC0 | ((c >> 6) & 0x1F))
                out += chr(0x80 | ((c >> 0) & 0x3F))
        return out

    def get_video(self):
        url = self.info['url'].replace('http://', 'http:##')
        url = base64.b64encode(self.__utf16to8(url))
        temp = Requests(url=self.api + url).request().decode('utf8')
        html = temp[157:-74]
        soup = BeautifulSoup(html)
        video = []
        score = 0
        for div in soup.select('div.panel'):
            if len(div.select('.glyphicon-subtitles')) > 0:
                self.dan_mu = div.select('p a')[0].attrs['href']
            else:
                head = div.select('.panel-heading')
                body = div.select('.panel-body')
                infos = head[0].select('code')
                if len(infos) > 0:
                    [section, clarity, sFormat] = infos[0].getText().split('_')
                    t = self.section_priority.get(section.encode('utf8'), 0)
                    t += self.clarity_priority.get(clarity.encode('utf8'), 0)
                    t += self.format_priority.get(sFormat, 0)
                    if score < t:
                        score = t
                        video = []
                        for p in body[0].select('p'):
                            video.append(p.select('a.file_url')[0].attrs['href'])
                            # 通过获取进一步的详细信息
                            # p.select('code')
        if len(video) == 0:
            logger.error('Can\'t search video in {0}'.format(soup))

        return video

    def get_ass(self):
        m = DanMuManager()
        if m.can_do(self.site):
            # return m.trans(self.site, 'http://static.comment.acfun.mm111.net/2266943-0')
            return m.trans(self.site, self.dan_mu)
        else:
            return None

    def get_ass_path(self):
        ass_text = self.get_ass()
        if ass_text is not None:
            path = '{0}{1}-{2}.ass' \
                .format(self.save_path, 'temp', int(time.time())) \
                .replace(' ', '')
            file = open(path, 'w')
            file.write(ass_text)
            file.close()
            return path
        return None
