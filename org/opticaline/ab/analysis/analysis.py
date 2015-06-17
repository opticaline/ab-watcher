# -*- coding: utf-8 -*-
# coding=utf-8
from bs4 import BeautifulSoup
import time
from org.opticaline.ab.analysis.danmu2ass import DanMuManager
import base64
from org.opticaline.ab.search.search import Ajax

__author__ = 'opticaline'


class Analysis:
    info = None
    api = 'http://flvsp.sinaapp.com/getData.php?url='
    dan_mu = None
    section_priority = {'单段': 0.8, '分段': 0.6}
    clarity_priority = {'原画': 10, '超清': 8, '高清': 6, '标清': 4, '低清': 2}
    format_priority = {'M3U8': -20, 'FlV': 0.06, 'MP4': 0.08}

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        temp = self.info['url'].replace('http://', '').split('/')[0].split('.')
        self.site = temp[len(temp) - 2]

    def get_video(self):
        url = self.info['url'].replace('http://', 'http:##')
        url = base64.b64encode(url.encode()).decode()
        temp = Ajax().get(self.api + url)
        # temp = Ajax(False).get('http://localhost:63342/ab-watcher/getData.html')
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
                    t = self.section_priority.get(section, 0)
                    t += self.clarity_priority.get(clarity, 0)
                    t += self.format_priority.get(sFormat, 0)
                    if score < t:
                        score = t
                        video.clear()
                        for p in body[0].select('p'):
                            video.append(p.select('a.file_url')[0].attrs['href'])
                            # 通过获取进一步的详细信息
                            # p.select('code')
        if len(video) == 0:
            print(soup)

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
            path = '/Users/Xu/{0}-{1}.ass'.format(self.info['title'], int(time.time())).replace(' ', '')
            file = open(path, mode='x', encoding='utf-8')
            file.write(ass_text)
            file.close()
            return path
        return None
