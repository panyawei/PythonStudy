#?-*-?coding:?utf-8?-*-??
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     17/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pypinyin import (lazy_pinyin,pinyin)
import pypinyin
name=raw_input()
print type(name)
while(len(name))==3:
    for i in range(len(name)):
        if i==0:
            name1= list(name)[i]
            a1= pypinyin.slug(name1)
            b1=list(a1)[0:2]
##            print b1
        if i==1:
            name2= list(name)[i]
            a2= pypinyin.slug(name2)
            b2=list(a2)[0:1]
##            print b2
        if i==2:
            name3= list(name)[i]
            a3= pypinyin.slug(name3)
            b3=list(a3)[0:1]
##            print b3
    print str(b1+b2+b3).upper()
    break

while(len(name))==2:
    for i in range(len(name)):
        if i==0:
            name1= list(name)[i]
            a1= pypinyin.slug(name1)
            b1=list(a1)[0:2]
##            print b1
        if i==1:
            name2= list(name)[i]
            a2= pypinyin.slug(name2)
            b2=list(a2)[0:2]
            print b2
    print str(b1+b2).upper()
    break

while(len(name))==4:
    for i in range(len(name)):
        if i==0:
            name1= list(name)[i]
            a1= pypinyin.slug(name1)
            b1=list(a1)[0:1]
##            print b1
        if i==1:
            name2= list(name)[i]
            a2= pypinyin.slug(name2)
            b2=list(a2)[0:1]
##            print b2
        if i==2:
            name3= list(name)[i]
            a3= pypinyin.slug(name3)
            b3=list(a3)[0:1]
##            print b3
        if i==3:
            name4= list(name)[i]
            a4= pypinyin.slug(name4)
            b4=list(a4)[0:1]
##            print b4
    print str(b1+b2+b3+b4).upper()
    break








