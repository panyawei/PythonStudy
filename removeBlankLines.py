#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     21/03/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
path='D:/...xml'
infopen = open(path,'r')
lines = infopen.readlines()
infopen.flush()
infopen.close()
outfopen = open(path,'w')
for line in lines:
    if line.split():
        outfopen.writelines(line)
    else:
        outfopen.writelines("")
outfopen.close()
