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
import re
def main():
    s = 'i,am,lilei'
    print s[2:4]
    ls=s.split(',')
    print ls
    print type(ls)
    print ls[1]

    a = 'aAsmk3AF'
    print len(a)
    print a[::-1]

    s = 'i love php'
    a = s.replace('i','I')
    print a.replace('php','python')



    strinfo = re.compile('php')
    b = strinfo.sub('python',s)
    print b






if __name__ == '__main__':
    main()
