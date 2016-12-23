# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     23/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import xml.dom.minidom
#打开xml文档
dom = xml.dom.minidom.parse('pred.xml')
#获取文档元素对象
root = dom.documentElement

#获取标签
print root.nodeName
print root.nodeValue
print root.nodeType

#获取子标签
bb = root.getElementsByTagName('pt')
b1 = bb[0]
b2 = bb[1]
print b1.nodeName

#获取标签属性值
val1 = b1.getAttribute('id')
val2 = b2.getAttribute('id')
print val1
print val2

#获取标签之间的数据
rn = root.getElementsByTagName('rn')
print rn[0].firstChild.data
print rn[1].firstChild.data






