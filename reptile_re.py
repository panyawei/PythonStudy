# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        使用正则表达式匹配字符串
# Purpose:
#
# Author:      Panywa
#
# Created:     11/05/2017
# Copyright:   (c) Panywa 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
pattern="yue"
string="http://yum.iqianyue.com"
# match函数从源字符串的开头进行匹配
# search函数则在全文中检索并匹配
result=re.search(pattern,string)
print (result.span())
if result:
    print result.group(0)
