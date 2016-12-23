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
    a = [11,22,24,29,30,32]
    a.append(28)
    print a
    a.insert(4,57)
    print a
    # 替换
    a[0]=6
    print a

if __name__ == '__main__':
    main()
