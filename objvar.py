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
    '''Represents a person'''
    population = 0
    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializes %s)' % self.name
        Person.population += 1

    def __del__(self):
        '''I am dying'''
        print '%s says bye' % self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one'
        else:
            print 'there are still %d people left' % Person.population

    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print 'Hi,my name is %s.' % self.name

    def howMany(self):
        '''prints the current population'''
        if Person.population ==1:
            print 'I am the only perple here'
        else:
            print 'we have %d peoples here' % Person.population

Tom = Person('Tom')
Tom.sayHi()
Tom.howMany()

Lucy = Person('Lucy')
Lucy.sayHi()
Lucy.howMany()
Lucy.__del__()

Tom.sayHi()
Tom.howMany()




