# coding: utf-8

import urllib
import re

def getlang():
    s = unicode(urllib.urlopen("http://ja.wikipedia.org/wiki/プログラミング言語一覧").read(),'utf-8')
    return re.findall(r'<li><a.*?>(.*?)</a></li>',s)

lang = getlang()

for l in lang:
    res = urllib.urlopen((u'http://www.google.com/complete/search?hl=ja&output=toolbar&ie=utf_8&oe=utf_8&q=%s くそ'%l).encode('utf-8')).read()
    if '糞言語' in res:
        print u'%sは糞言語'%l
    #else:
    #    print u'%sは糞言語ではない'%l
