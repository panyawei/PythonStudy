# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:
#
# Created:     21/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    ab = { 'Swaroop' : 'swaroopch@byteofpython.info',
           'Larry' : 'larry@wall.org',
           'Matsumoto' : 'matz@ruby-lang.org',
           'Spammer' : 'spammer@hotmail.com'
         }
    print "Swaroop's address is %s" % ab['Swaroop']   # return value
    # append
    ab['Guido'] = 'guido@python.org'
    print ab
    # delete
    del ab['Spammer']
    print ab
    # traverse
    for name, address in ab.items():
        print 'Contact %s at %s' % (name, address)

if __name__ == '__main__':
    main()
