#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     14/03/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import traceback
import os
class Test:
    def A(self):
        try:
            a=b
            b=c
        except Exception,e:
            print Exception,":",e
            Test.B(self)
    def B(self):
        if not os.path.exists('E:/log'):
            os.makedirs('E:/log')
        path=os.path.join('/log','log.txt')
        f=open(path,'a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()
if __name__=='__main__':
    test=Test()
    test.A()