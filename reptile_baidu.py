# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        爬取百度首页
# Purpose:
#
# Author:      Panywa
#
# Created:     10/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib import urlopen,quote,unquote

files=urlopen("http://www.baidu.com")
#获取网页的状态码，200为正常的
print files.getcode()
#获取网页的url
print files.geturl()
#返回与当前环境有关的信息  爬取的网页.info()
print files.info()
# 对某网址编码 urllib.request.quote()
sina=quote("http://www.sina.com.cn")
print sina
# 对某网址解码 urllib.request.unquote()
unsina=unquote(sina)
print unsina
date=files.read()
dateline=files.readline().decode("utf-8")
#print (date)
handledate=open("G:/AA.html","wb")
handledate.write(date)
handledate.close()
