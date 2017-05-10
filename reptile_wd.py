# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        检索关键词为hello的结果
# Purpose:
#
# Author:      Panywa
#
# Created:     10/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib import urlopen

keywd="余润泽"
url="http://baidu.com/s?wd="+keywd
data=urlopen(url).read()
handle=open("G:/cc.html","wb")
handle.write(data)
handle.close()
