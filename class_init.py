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

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print 'my name is',self.name

p = Person('Tom')
p.sayHi()

