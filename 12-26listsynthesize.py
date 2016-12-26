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

def main():
    lis1 = [2,6,3]
    lis2 = [2*i for i in lis1 if i>2]
    print lis2   #list
    for i in lis2:
        print i  #int

if __name__ == '__main__':
    main()
