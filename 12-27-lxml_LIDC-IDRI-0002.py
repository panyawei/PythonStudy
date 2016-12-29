# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     27/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lxml import etree
tree_LIDC = etree.parse('LIDC-IDRI-0002.xml')  # 解析成树
root_LIDC = tree_LIDC.getroot()   # 获取指定节点节点
print root_LIDC  # <Element boost_serialization at 0x3503dc8>
# 遍历
for articel in root_LIDC:
    print  u'元素名称：',articel.tag  # 获取子元素的名称
##    # 遍历子元素
##    for field in articel:
##        # 用.tag可以得到元素的名称，而.text可以得到元素的内容
##        print field.tag,'==>',field.text
##    # 用.get("属性名")可以得到元素相应属性的值
##        class_id = field.get('class_id')
##        print  u'元素属性id',class_id

##Tag = tree_LIDC.xpath('//Nodules')
tree_xmlformat = etree.parse('xmlformat.xml')
root_xmlformat = tree_xmlformat.getroot()
print root_xmlformat
for xmlformat in root_xmlformat:
    print xmlformat.tag
##    if xmlformat.tag == 'VerifiedNodules':
    a = etree.SubElement(articel.tag,xmlformat.tag)
##        etree.tostring(root_xmlformat, pretty_print=True)
    for item in xmlformat:
            b = etree.SubElement(a,item.tag)
    ##        print item.tag
            for element in item:
                print element.tag,'==>',element.text
                c = etree.SubElement(b,element.tag)
                c.text = element.text
                etree.tostring(root_LIDC, pretty_print=True)
                tree_LIDC = etree.ElementTree(root_xmlformat)

##    elif xmlformat.tag == 'MissedNodules':
##        a = etree.SubElement(root_LIDC,xmlformat.tag)
##        for item in xmlformat:
##            b = etree.SubElement(a,item.tag)
##            for element in item:
##                print element.tag,'==>',element.text
##                c = etree.SubElement(b,element.tag)
##                c.text = element.text
##                etree.tostring(root_xmlformat, pretty_print=True)

                f = file('E:\github\python\PythonStudy\LIDC-IDRI-0002.xml','a')
                tree_LIDC.write(f,pretty_print=True)



