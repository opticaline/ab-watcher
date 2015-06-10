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
        analysis = Analysis(info=array[0])
        print(analysis.get_video())
