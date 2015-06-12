from bs4 import BeautifulSoup
from org.opticaline.ab.analysis.danmu2ass import DanMuManager
import base64
from org.opticaline.ab.search.search import Ajax

__author__ = 'opticaline'


class Analysis:
    info = None
    api = 'http://flvsp.sinaapp.com/getData.php?url='
    dan_mu = None

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        temp = self.info['url'].replace('http://', '').split('/')[0].split('.')
        self.site = temp[len(temp) - 2]

    def get_video(self):
        url = self.info['url'].replace('http://', 'http:##')
        url = base64.b64encode(url.encode()).decode()
        temp = Ajax().get(self.api + url)
        # temp = Ajax(False).get('http://localhost:63342/AB/getData.html')
        html = temp[157:-74]
        soup = BeautifulSoup(html)
        video = []
        for div in soup.select('div.panel'):
            if len(div.select('.glyphicon-subtitles')) > 0:
                self.dan_mu = div.select('p a')[0].attrs['href']
            elif str(div).find('原画') != -1:
                for a in div.select('div.panel-body p a'):
                    video.append(a.attrs['href'])
                break
        return video

    def get_ass(self):
        m = DanMuManager()
        if m.can_do(self.site):
            return m.trans(self.site, self.dan_mu)
        else:
            return None
