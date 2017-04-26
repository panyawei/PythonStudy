# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     18/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def GetFileList(dir,fileList):
    import os
    newDir= dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir,fileList)
    return fileList
##if __name__ == '__main__':
lis=GetFileList('D:\ZSDicoms\Puncture_CT',[])
for e in lis:
    print e#[33:-5]