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
import os,shutil
import re
import pypinyin

dir_path=u'D:\Puncture_CT\PuntureSouthwest Hospital_CT'
files=[x for x in os.listdir(dir_path)]
output_file= u'D:\Puncture_CT'
for ii in files:
    filess = re.split(r'(\W+)',ii)
    name=filess[1]

    for num in range(1,1236):
        if str(filess).startswith('[u\'%s\'' % num) :
            if filess[0]==str(num):
                while(len(name))==3:
                    for i in range(len(name)):
                        if i==0:
                            name1= list(name)[i]
                            a1= pypinyin.slug(name1)
                            namelist=list(a1)
                            b1=namelist[0]+namelist[1]
                        if i==1:
                            name2= list(name)[i]
                            a2= pypinyin.slug(name2)
                            namelist=list(a2)
                            b2=namelist[0]
                        if i==2:
                            name3= list(name)[i]
                            a3= pypinyin.slug(name3)
                            namelist=list(a3)
                            b3=namelist[0]
                    nameUpper=(b1+b2+b3).upper()
                    path=r"D:/Puncture_CT/%s%s/" %(filess[0],nameUpper)
                    isExists=os.path.exists(path)
                    if not isExists:
                        os.mkdir(path)
                        shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    break
                while(len(name))==2:
                    for i in range(len(name)):
                        if i==0:
                            name1= list(name)[i]
                            a1= pypinyin.slug(name1)
                            namelist=list(a1)
                            b1=namelist[0]+namelist[1]
                        if i==1:
                            name2= list(name)[i]
                            a2= pypinyin.slug(name2)
                            namelist=list(a2)
                            b2=namelist[0]+namelist[1]
                    nameUpper= (b1+b2).upper()
                    path=r"D:/Puncture_CT/%s%s/" %(filess[0],nameUpper)
                    isExists=os.path.exists(path)
                    if not isExists:
                        os.mkdir(path)
                        shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    break
                while(len(name))==4:
                    for i in range(len(name)):
                        if i==0:
                            name1= list(name)[i]
                            a1= pypinyin.slug(name1)
                            namelist=list(a1)
                            b1=namelist[0]
                        if i==1:
                            name2= list(name)[i]
                            a2= pypinyin.slug(name2)
                            namelist=list(a2)
                            b2=namelist[0]
                        if i==2:
                            name3= list(name)[i]
                            a3= pypinyin.slug(name3)
                            namelist=list(a3)
                            b3=namelist[0]
                        if i==3:
                            name4= list(name)[i]
                            a4= pypinyin.slug(name4)
                            namelist=list(a4)
                            b4=namelist[0]
                    nameUpper= (b1+b2+b3+b4).upper()
                    path=r"D:/Puncture_CT/%s%s/" %(filess[0],nameUpper)
                    isExists=os.path.exists(path)
                    if not isExists:
                        os.mkdir(path)
                        shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    shutil.copy(dir_path+'\\''%s%s%s.dcm' %(filess[0],filess[1],filess[2]),path+'\\'+filess[0]+nameUpper+filess[2]+'.dcm')
                    break








