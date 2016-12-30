#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     30/12/2016
# Copyright:   (c) 12SigmaTech 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
g='Green'
t=' trees'
print g+t

bird='Sparrow'
beast=u'Unicorn'
print type(bird),type(beast),type(bird+beast)  #<type 'str'> <type 'unicode'> <type 'unicode'>

# character string reverse conversion   string ==>ASCII or Unicode
euro=unichr(1314) #unichr(int)
print ord(euro)  #  ord()  reverse conversion

# character string is ordered set
phrase='The red balloon'
print phrase[0],phrase[2],phrase[-1]   # T e n
# support slicing
print phrase[:3],phrase[1:5],phrase[-3:],phrase[-3:-1]  #The  he r oon oo
# character string is immutable
##phrase[0]='a'
##print phrase  TypeError: 'str' object does not support item assignment

# Method of insertion characters
p1='pad'
p1=p1[:1]+'o'+p1[2:]
print 'p1',p1   # pod

p2='pad'
p2='o'.join((p2[:1],p2[2:]))
print 'p2',p2   # pod

# Access to index values by function
p3=p2.find('d')
print p3  #  2  if false return -1

##p4=p2.index('a')
##print p4 # if false return ValueError:substring not found


# QString is alterable
from PyQt4.QtCore import *
a=QString('apple')
b=unicode('baker')
print a+b,type(a+b) # applebaker PyQt4.QtCore.QString




