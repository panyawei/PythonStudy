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

from xml.etree import ElementTree as ET
dom = ET.parse('pred.xml')
d = dom.findall('./sri')
for s in d:
    for child in s.getchildren():
        print child.tag,child.text