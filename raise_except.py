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
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
    print 'ShortInputException:The input was of length %d.\
        was excepting at least %d' %(x.length,x.atleast)
else:
    print 'No exception was raised'