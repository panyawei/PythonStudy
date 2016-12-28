# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Panywa
#
# Created:     28/12/2016
# Copyright:   (c) Panywa 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lxml import etree
tree_LIDC = etree.parse('LIDC-IDRI-0002.xml')  # 解析成树
root_LIDC = tree_LIDC.getroot()

print root_LIDC
tree_xmlformat = etree.parse('xmlformat.xml')
root_xmlformat = tree_xmlformat.getroot()
print root_xmlformat
###遍历LIDC-IDRI-0002.xml文件
##for articel in root_LIDC:
##    print articel
#遍历xmlformat.xml
for xmlformat in root_xmlformat:
    print xmlformat.tag
    if xmlformat.tag == 'VerifiedNodules':
        print 'VerifiedNodules stage'
        a = etree.SubElement(root_LIDC,xmlformat.tag)
        for item in xmlformat:
            b = etree.SubElement(a,item.tag)
            for element in item:
                print element.tag,'==>',element.text
                c = etree.SubElement(b,element.tag)
                c.text = element.text
                etree.tostring(root_xmlformat, pretty_print=True)
                tree_LIDC = etree.ElementTree(root_LIDC)
                f = file('E:\github\python\PythonStudy\LIDC-IDRI-00010.xml','w')
                tree_LIDC.write(f,pretty_print=True)
    elif xmlformat.tag =='MissedNodules':
        print 'MissedNodules stage'
        a = etree.SubElement(root_LIDC,xmlformat.tag)
        for item in xmlformat:
            b = etree.SubElement(a,item.tag)
            for element in item:
                print element.tag,'==>',element.text
                c = etree.SubElement(b,element.tag)
                c.text = element.text
                etree.tostring(root_xmlformat, pretty_print=True)
                tree_LIDC = etree.ElementTree(root_LIDC)
                f = file('E:\github\python\PythonStudy\LIDC-IDRI-00010.xml','w')
                tree_LIDC.write(f,pretty_print=True)
