# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     26/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from xml.etree.ElementTree import parse,ElementTree,Element
doc1 = parse('LIDC-IDRI-0002.xml')
root = doc.getroot()
doc2 = parse('xmlformat')


##print root[0]   # Nodules
VerifiedNodules = Element('VerifiedNodules')


##root.getchildren().index(root.find('Nodules'))
##VerifiedNodules = Element('VerifiedNodules')
VerifiedNodules.text= 'ok'
##root.insert(1,VerifiedNodules)
##doc1.write(f)

##from xml.dom import minidom
##import xml.etree.ElementTree as EF
##impl = minidom.getDOMImplementation()
##dom = impl.createDocument(None, None, None)
