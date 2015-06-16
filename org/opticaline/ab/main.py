from mplayer.player import Player
from org.opticaline.ab.analysis.analysis import Analysis
from org.opticaline.ab.search.searchmanager import SearchManager

__author__ = 'opticaline'
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-a", "--acfun", action="store_false", dest="GetAcFun", default=True,
                      help="Get movies from AcFun.tv")
    parser.add_option("-b", "--bilibili", action="store_false", dest="GetBilibili", default=True,
                      help="Get movies from BiliBili.tv")
    parser.add_option("-c", "--cache", action="store_false", dest="Cache", default=0,
                      help="Cache the website result")
    parser.add_option("-s", "--source", dest="Source", metavar="FILE", default="../../../config/source.json",
                      help="write report to FILE")
    (options, args) = parser.parse_args()
    if len(args) > 0:
        manager = SearchManager(options)
        array = manager.search(args)
        #
        analysis = Analysis(info=array[0])
        video = analysis.get_video()
        # video = [
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_01/st/flv/fileid/030002070051B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=53e143514d341d9e261e663a&hd=0&ts=382&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfL6xAyReQSB5GgW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_02/st/flv/fileid/030002070151B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=8a3ea9c81c4a9274282a8f1e&hd=0&ts=368&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfLf67e9pkPqM2gW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_03/st/flv/fileid/030002070251B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=1beaa030b8266d4e24123d56&hd=0&ts=413&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfLzanxcL4hfkSgW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_04/st/flv/fileid/030002070351B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=6f855f7a983b8845261e663a&hd=0&ts=377&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfLkSabBuqrciygW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_05/st/flv/fileid/030002070451B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=7fd43e1509b33616282a8f1e&hd=0&ts=373&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfL2CjItL69RGGgW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_06/st/flv/fileid/030002070551B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=40d1f28f2004c7f6282a8f1e&hd=0&ts=246&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfLSKRX7TQtefSgW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96',
        #     'http://k.youku.com/player/getFlvPath/sid/943442035527651f185be_07/st/flv/fileid/030002070651B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE?K=3a560d4c779b73a9261e663a&hd=0&ts=243&ctype=51&token=5079&ev=1&oip=2086526472&ep=Hi6YWlCnw20leYDEz2WKAcC6y%2FoTdFfLoam5sYF2JpGgW0K3XJx4gseM4vM1No%2FUbTw61j%2BlatWs0%2FNG2WfbSMnvLBL2QngZnfzi2cB0El0zM1QZ64NmvzD94GM5Nf96']
        video = [
            'D:/videos/030002070051B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE.flv',
            'D:/videos/030002070151B73A9E98BF092DCCF7C9A88F01-0874-FE72-5F14-C8648EF519CE.flv',
        ]
        subtitle = analysis.get_ass_path()
        Player().play(video, subtitle, array[0]['title'])
