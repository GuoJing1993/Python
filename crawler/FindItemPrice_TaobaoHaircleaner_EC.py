# -*- coding: utf-8 -*-
import urllib
import re

page=0
while page<180:
    url='https://s.taobao.com/list?spm=a21bo.7724922.8383.27.Tna8jH&q=%E6%B4%97%E5%8F%91%E6%B0%B4&cat=1801%2C50071436%2C50010788&seller_type=taobao&bcoffset=0&style=list&s='+str(page)
    opener= urllib.urlopen(url).read()
    names= re.findall('"raw_title":"(.*?)","pic_url":',opener)
    for name in names:
        print name
    int(page)
    page=page+30
