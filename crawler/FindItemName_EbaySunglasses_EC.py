# -*- coding: utf-8 -*-
import urllib
import re

page=int(1)
num=0
total=0
while page<10:
    url='http://www.ebay.com/rpp/moda-en/GEO-EG-Sunglasses-Freeship/?_pgn='+str(page)
    opener= urllib.urlopen(url).read()
    names= re.findall('<span class="rttl">(.*?)</span>',opener)
    for name in names:
        total=total+1
        brands= name.split()
        for brand in brands:
            if brand=='NIKE':
                num=num+1
        print name
    print float(num)/total
    int(page)
    page=page+1
