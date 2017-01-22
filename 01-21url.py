# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        url
# Purpose:
#
# Author:      Panywa
#
# Created:     21/01/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib import quote,quote_plus,unquote,unquote_plus
from urllib import urlencode
#  编码
r1=quote('/~test/')
print r1
r2=quote('/~test/public html')
print r2  # /%7Etest/public%20html
r3=quote_plus('/~test/public html')
print r3  # %2F%7Etest%2Fpublic+html   # 将/ ~ 空格 等都编码

r4=quote('我爱中国')
print (u'对中文的编码:'),r4

#  解码
print unquote(r2)
print unquote_plus(r3)

print (u'对中文的解码:'),unquote(r4).decode('utf-8')   #  解决乱码问题


#  其他
a = urlencode([('keyword1','value1'),('keyword2','value2')])   # (key,value)
print a  # keyword1=value1&keyword2=value2   # 建议使用列表，因为dict是无序的

b = urlencode({'key1':'value1','key2':'value2'})   # dict 字典  无序
print b   # key2=value2&key1=value1

a1=urlencode([('key',('val1','val2','val3','val4'))])   # 默认参数值为false
print a1  # key=%28%27val1%27%2C+%27val2%27%2C+%27val3%27%2C+%27val4%27%29

a2=urlencode([('key',('val1','val2','val3','val4'))],True)
print a2  # key=val1&key=val2&key=val3&key=val4

print unquote_plus(a1)
