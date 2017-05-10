# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        设置代理服务器去爬取网站
# Purpose:
#
# Author:      Panywa
#
# Created:     10/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def use_proxy(proxy_addr,url):
    from urllib2 import ProxyHandler,build_opener,HTTPHandler,install_opener,urlopen,HTTPError
    try:
        proxy=ProxyHandler({'http':proxy_addr})
        opener=build_opener(proxy,HTTPHandler)
        install_opener(opener)
        data=urlopen(url).read().decode("utf-8")
        return data
    except HTTPError as e:
        data= e.code+e.reason
        print data
        return data
proxy_addr='183.78.183.156:82'
data=use_proxy(proxy_addr,"http://www.baidu.com")
print (data)