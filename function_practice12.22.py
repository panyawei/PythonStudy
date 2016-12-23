# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     22/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
def func(name,callback=None):
    if callback==string.lower:
        print name.lower()
    elif callback==string.upper:
        print name.upper()
    else:
        print name.capitalize()  # 首字母大写
func('lilei')
func('LILEI',callback=string.lower)
func('lilei',callback=string.upper)
