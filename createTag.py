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



##import xml.etree.ElementTree as EF
##a = EF.Element('newstart1')
##dom = EF.parse('pred.xml')

##b = EF.SubElement(a,'name')
##b.attrib = {'name':'name attribute'}
##b.text = 'wangwu'
##c = EF.SubElement(a,'age')
##c.text = '25'
##f = file('E:\PyScriptcx\pred.xml','a')
##tree = EF.ElementTree(a)
##tree.write(f)
##f.close()



from xml.dom import minidom
impl = minidom.getDOMImplementation()
print impl
dom = impl.createDocument(None, None, None)
newstart = dom.createElement('newstart3')
name = dom.createElement('name')
name.appendChild(dom.createTextNode('zhangqiang'))
newstart.appendChild(name)
age = dom.createElement('age')
age.appendChild(dom.createTextNode('25'))
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