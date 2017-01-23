#-------------------------------------------------------------------------------
# Name:        extracting files
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     23/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os,re,shutil
dir_path=u'D:\zhongshan_data20170111\ZSCT02_Nii'
output_file=u'D:\zhongshan_data20170111\WriteIn\ZSCT02_Nii'
files=[x for x in os.listdir(dir_path)]
for ii in files:
    filess=re.split(r'\.',ii)
    if filess[1]=='xml':
        path=r"%s/" %(output_file)
        isExists=os.path.exists(path)
        if not isExists:
            os.mkdir(path)
            shutil.copy(dir_path+'\\''%s.xml' % filess[0],path+'\\'+filess[0]+'.xml')
        shutil.copy(dir_path+'\\''%s.xml' % filess[0],path+'\\'+filess[0]+'.xml')