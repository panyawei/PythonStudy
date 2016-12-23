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
    zoo=('wolf','elephant','cat')
    print 'number of zoo is',len(zoo)
    new_zoo=('dog','mouse',zoo)
    print 'number of zoo is',len(new_zoo)
    print new_zoo
    print new_zoo[0]
    print new_zoo[2]
    print new_zoo[2][2]

    age = 22
    name = 'Swaroop'
    print '%s is %d years old' % (name, age)
    print 'Why is %s playing with that python?' % name

if __name__ == '__main__':
    main()
