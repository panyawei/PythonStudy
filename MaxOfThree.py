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

def max(a,b,c):
##    global a,b,c
    if a>b:
        if a>c:
            print a,'is Max'
            if b>c:
                t=a
                a=c
                c=t
                print 'a=',a
                print 'b=',b
                print 'c=',c
            else:
                t=a
                a=b
                b=c
                c=t
                print 'a=',a
                print 'b=',b
                print 'c=',c
        else:
            print c,'is Max'
            t=a
            a=b
            b=t
            print 'a=',b
            print 'b=',t
            print 'c=',c
    elif b>c:
        print b,'is Max'
        if a>c:
            t=a
            a=c
            c=b
            b=t
            print 'a=',b
            print 'b=',c
            print 'c=',t
        else:
            t=b
            b=c
            c=t
            print 'a=',a
            print 'b=',b
            print 'c=',t
    else:
        print c,'is Max'
        print 'a=',a
        print 'b=',b
        print 'c=',c
a = int(raw_input('Enter one number'))
b = int(raw_input('Enter one number'))
c = int(raw_input('Enter one number'))
max(a,b,c)



##if __name__ == '__main__':
##    max(a,b,c)
