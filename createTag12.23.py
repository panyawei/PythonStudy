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
##from xml.etree.ElementTree import parse, Element,ElementTree
##doc = parse('pred.xml')
##root = doc.getroot()
####root.remove(root.find('sri'))
##root.find('./nm').text = '12'
##root.getchildren().index(root.find('nm'))
##e = Element('spam')
##e.text = 'This is a test'
##root.insert(2, e)
##
##doc.write('pred.xml', xml_declaration=True)


from xml.dom import minidom
impl = minidom.getDOMImplementation()
print impl
dom = impl.createDocument(None, None, None)
newstart = dom.createElement('newstart')
name = dom.createElement('name')
print type(name)
age = dom.createElement('age')

newstart.appendChild(name)

newstart.appendChild(age)

dom.appendChild(newstart)
f = file('E:\PyScriptcx\pred.xml','a')
dom.writexml(f,'',' ','\n','utf-8')
f.close()











##from xml.etree import ElementTree
##filepath = 'E:\PyScriptcx\pred.xml'
##dom = ElementTree.parse(filepath)
##name = dom.find('./id')##
##name.text = "5"