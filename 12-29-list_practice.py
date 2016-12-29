# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Panywa
#
# Created:     29/12/2016
# Copyright:   (c) Panywa 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
lista=[12,3,21,6,4,15]
listb=[]
print lista
##a = raw_input('Enter one integer')
if 6 in lista:
    index = lista.index(6)
    print index
    lista.pop(index)
    lista.sort()
    for i in lista:
        if i>6:
            listb.append(i-1)
        else:
            listb.append(i)
lista=listb
print lista

