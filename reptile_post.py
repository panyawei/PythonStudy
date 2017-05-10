# -*- coding?utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ??post??
# Purpose:
#
# Author:      Panywa
#
# Created:     10/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib import urlencode,urlopen
from urllib2 import Request,build_opener
import urllib2
url="http://www.iqianyue.com/mypost/"
##postdata=urlencode({"name":"panyawei","pass":"203010"},).encode("utf-8")
##req=urllib2.Request(url,postdata)
header=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
     51.0.2704.79 Safari/537.36 Edge/14.14393")
# ??????opener??
opener=build_opener()
# ?????
opener.addheaders=[header]
data=opener.open(url).read()
handle=open("G:/dd.html","wb")
handle.write(data)
handle.close()

