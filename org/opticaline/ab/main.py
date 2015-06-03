from org.opticaline.ab.search.searchmanager import SearchManager

__author__ = 'opticaline'
from optparse import OptionParser


def getargs():
    parser = OptionParser()
    parser.add_option("-a", "--acfun", action="store_false", dest="GetAcFun", default=True,
                      help="Get movies from AcFun.tv")
    parser.add_option("-b", "--bilibili", action="store_false", dest="GetBilibili", default=True,
                      help="Get movies from BiliBili.tv")
    parser.add_option("-c", "--cache", action="store_false", dest="Cache", default=0,
                      help="Cache the website result")
    parser.add_option("-s", "--source", dest="Source", metavar="FILE", default="../../../config/source.json",
                      help="write report to FILE")
    return parser.parse_args()


if __name__ == '__main__':
    (options, args) = getargs()
    if len(args) > 0:
        manager = SearchManager(options)
        print(manager.search(args))
