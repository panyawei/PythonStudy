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
result=re.search(pattern,string)
print result
