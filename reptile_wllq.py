# -*- coding?utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ??????????
# Purpose:
#
# Author:      Panywa
#
# Created:     10/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib import urlopen
from urllib2 import build_opener
#url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
#files=urlopen(url)
#data=files.read().decode("utf-8")
#print data
# ??????????????????????????

url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
     51.0.2704.79 Safari/537.36 Edge/14.14393")
# ??????opener??
opener=build_opener()
# ?????
opener.addheaders=[headers]
data=opener.open(url).read()
handle=open("G:/bb.html","wb")
handle.write(data)
handle.close()
