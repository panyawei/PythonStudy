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
def powersum(power,*args):
    total = 0
    for i in args:
        total += pow(i,power)  #pow(n,m)==>n的m次方
    print total
    return total
powersum(2,4,3)
powersum(2,100)

