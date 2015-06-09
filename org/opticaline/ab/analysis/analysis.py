from org.opticaline.ab.analysis.danmu2ass import HANDLE_SET
import base64
from org.opticaline.ab.search.search import Ajax

__author__ = 'opticaline'


class Analysis:
    info = None
    api = 'http://flvsp.sinaapp.com/getData.php?url='

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        temp = self.info['url'].replace('http://', '').split('/')[0].split('.')
        self.site = temp[len(temp) - 2]

    def get_video(self):
        url = base64.b64encode(self.info['url'].replace('http://', 'http:##').encode()).decode()
        print(self.info['url'].replace('http://', 'http:##'))
        print(Ajax().get(self.api + url))

    def get_ass(self):
        if self.site in HANDLE_SET.keys():
            print(HANDLE_SET[self.site])
        else:
            return None
