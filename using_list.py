# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     21/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    shoplist=['v','d','c']
    # append
    shoplist.append('a')
    print shoplist
    # return length
    print len(shoplist)
    # traverse
    for i in shoplist:
        print i,

    print ''
    # sort
    shoplist.sort()
    print shoplist
    # obtain the subscript
    print shoplist[0]
    # delete
    del shoplist[0]
    print shoplist


if __name__ == '__main__':
    main()
