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

def get_num(num):
    lis = []
    for t in num:
        if type(t)!=int:
            print 'Error'
            break
        else:
           if (t % 2)==0:
                lis.append(t)
    print lis

string = int(input(u"请输入次数"))
num = []
for i in range(string):
    i = input('Enter one:')
    num.append(i)
get_num(num)



