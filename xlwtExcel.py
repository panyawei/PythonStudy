# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     10/02/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlwt
from xlwt import *
w=Workbook(encoding='utf-8')
sheet1=w.add_sheet('first')

alignment=Alignment()
alignment.center=True
style_top= XFStyle()
fnt_top= Font()
fnt_top
fnt_top.name = u'微软雅黑'
##fnt_top.alignment=True
fnt_top.bold= True

style_top.font= fnt_top


style_other=XFStyle()
fnt_other=Font()
fnt_other.name=u'微软雅黑'
##fnt_other.alignment=True
style_other.font=fnt_other
style_other.alignment=alignment

# 肺实质/气管/支气管异常
sheet1.write_merge(0,0,0,12,'ID编号：                  姓名：                 性别：男 女                  年龄：                 检查日期：   年   月    日',style_top)
sheet1.write_merge(1,11,0,2,'    肺实质/气管/支气管异常',style_top)
sheet1.write_merge(1,2,3,6,'                        病变/部位',style_other)
sheet1.write_merge(1,1,7,9,'              右侧(RS1-10)',style_other)
sheet1.write_merge(1,1,10,12,'            左侧(LS1-10)',style_other)
sheet1.write(2,7,'上',style_other)
sheet1.write(2,8,'中',style_other)
sheet1.write(2,9,'下',style_other)
sheet1.write(2,10,'上',style_other)
sheet1.write(2,11,'中',style_other)
sheet1.write(2,12,'下',style_other)
sheet1.write_merge(3,3,3,4,'肺实质/GGO',style_other)
row_column=[u'无',u'有',u'',u'',u'',u'',u'',u'']
i,j=0,3
for j in range(3,11):
    while i<len(row_column) and j!=10:
        sheet1.write(j,i+5,row_column[i],style_other)
        i+=1
    j+=1
    i=0


sheet1.write_merge(4,4,3,4,'树芽征/腺泡结节',style_other)
sheet1.write(11,5,'无',style_other)
sheet1.write(11,6,'有',style_other)
sheet1.write_merge(5,5,3,4,'纤维瘢痕/梗结',style_other)

sheet1.write_merge(6,6,3,4,'支气管扩张',style_other)

sheet1.write_merge(7,7,3,4,'肺间质纤维化',style_other)

sheet1.write_merge(8,8,3,4,'肺不张',style_other)

sheet1.write_merge(9,9,3,4,'肺气肿',style_other)

sheet1.write_merge(10,10,3,12,'附加描述:',style_other)
sheet1.write_merge(11,11,3,4,'气管/支气管',style_other)

sheet1.write(11,7,'结节',style_other)
sheet1.write_merge(11,11,8,9,'管壁增厚',style_other)
sheet1.write(11,10,'腔狭窄',style_other)
sheet1.write_merge(11,11,11,12,'部位:',style_other)

#  胸腔/胸膜异常
sheet1.write_merge(12,14,0,2,'              胸腔/胸膜异常',style_top)
columu_chest=[u'胸腔积液',u'胸膜增厚',u'胸膜斑']
i,j=0,12
while i<len(columu_chest):
    sheet1.write_merge(j,j,3,4,columu_chest[i],style_other)
    j+=1
    i+=1
row_chest_one=[u'无',u'有',u'右侧',u'左侧',u'双侧',u'少量',u'中量',u'大量']
i,j=0,12
while i<len(row_chest_one):
    sheet1.write(j,i+5,row_chest_one[i],style_other)
    i+=1
row_chest_two=[u'无',u'有',u'右侧',u'左侧',u'双侧',u'局限',u'广泛',u'钙化']
i,j=0,13
while i<len(row_chest_one):
    sheet1.write(j,i+5,row_chest_two[i],style_other)
    i+=1
sheet1.write(14,5,'无',style_other)
sheet1.write(14,6,'有',style_other)
sheet1.write_merge(14,14,7,12,'胸膜病变补充:',style_other)
# 心脏/大血管
sheet1.write_merge(15,20,0,2,'              心脏/大血管',style_top)
column_bloodvessel=[u'冠状动脉钙化',u'心包增厚',u'心包积液',u'心影增大',u'主动脉病变',u'肺动脉异常']
i,j=0,15
while i<len(column_bloodvessel):
    sheet1.write_merge(j,j,3,4,column_bloodvessel[i],style_other)
    i+=1
    j+=1
row_bloodvessel_one=[u'无',u'有',u'左主干',u'前降支',u'左旋支',u'右主干',u'',u'']
i,j=0,15
while i<len(row_bloodvessel_one):
    sheet1.write(j,i+5,row_bloodvessel_one[i],style_other)
    i+=1
row_bloodvessel_two=[u'无',u'有',u'局限',u'弥漫']
i,j=0,16
while i<len(row_bloodvessel_two):
    sheet1.write(j,i+5,row_bloodvessel_two[i],style_other)
    i+=1
sheet1.write_merge(16,16,9,12,'其它:',style_other)
row_bloodvessel_three=[u'无',u'有',u'局限',u'弥漫']
i,j=0,17
while i<len(row_bloodvessel_three):
    sheet1.write(j,i+5,row_bloodvessel_three[i],style_other)
    i+=1
sheet1.write_merge(17,17,9,12,'少量           中量          大量',style_other)
row_bloodvessel_four=[u'无',u'有',u'左心室',u'右心室',u'左心房',u'右心房',u'普大',u'其它']
i,j=0,18
while i<len(row_bloodvessel_four):
    sheet1.write(j,i+5,row_bloodvessel_four[i],style_other)
    i+=1
row_bloodvessel_five=[u'无',u'有',u'壁钙化',u'动脉瘤']
i,j=0,19
while i<len(row_bloodvessel_five):
    sheet1.write(j,i+5,row_bloodvessel_five[i],style_other)
    i+=1
sheet1.write_merge(19,19,9,12,'其它:',style_other)
row_bloodvessel_six=[u'无',u'有',u'左PA',u'右PA']
i,j=0,20
while i<len(row_bloodvessel_six):
    sheet1.write(j,i+5,row_bloodvessel_six[i],style_other)
    i+=1
sheet1.write_merge(20,20,9,12,'描述:',style_other)

# lymph gland
sheet1.write_merge(21,23,0,2,'      纵隔/肺门/其他部位淋巴结',style_top)
column_lbj=[u'淋巴结>=1cm',u'淋巴结<1cm',u'淋巴结钙化']
i,j=0,21
while i<len(column_lbj):
    sheet1.write_merge(j,j,3,4,column_lbj[i],style_other)
    i+=1
    j+=1
row_lbj=[u'无',u'有']
i,j=0,21
for j in range(21,24):
    while i<len(row_lbj):
        sheet1.write(j,i+5,row_lbj[i],style_other)
        i+=1
    j+=1
    i=0
j=21
for j in range(21,24):
    sheet1.write_merge(j,j,7,12,'部位:',style_other)
    j+=1

# mediastinumLesion
sheet1.write_merge(24,27,0,2,'              纵隔病变',style_top)
column_zgbb=[u'纵隔占位',u'食道病变',u'甲状腺病变']
i,j=0,24
while i<len(column_zgbb):
    sheet1.write_merge(j,j,3,4,column_zgbb[i],style_other)
    i+=1
    j+=1
sheet1.write_merge(27,27,3,12,'附加描述:',style_other)
row_zgbb=[u'无',u'有']
i,j=0,24
for j in range(24,27):
    while i<len(row_zgbb):
        sheet1.write(j,i+5,row_zgbb[i],style_other)
        i+=1
    j+=1
    i=0
sheet1.write_merge(24,24,7,12,'部位及描述:',style_other)
sheet1.write(25,7,'上段',style_other)
sheet1.write(25,8,'中段',style_other)
sheet1.write(25,9,'下端',style_other)
sheet1.write_merge(25,25,10,12,'补充:',style_other)
row_zgbb_three=[u'左叶',u'右叶',u'弥漫',u'实性',u'蘘性',u'其它:']
i,j=0,26
while i<len(row_zgbb_three):
    sheet1.write(j,i+7,row_zgbb_three[i],style_other)
    i+=1

# Chest wall lesion
sheet1.write_merge(28,30,0,2,'              胸壁病变',style_top)
sheet1.write_merge(28,28,3,4,'胸壁软组织',style_other)
sheet1.write_merge(29,29,3,4,'肋骨异常',style_other)
sheet1.write_merge(30,30,3,12,'附加描述:',style_other)
row_xbbb=[u'无',u'有',u'右侧',u'左侧']
i,j=0,28
for j in range(28,30):
    while i<len(row_xbbb):
        sheet1.write(j,i+5,row_xbbb[i],style_other)
        i+=1
    sheet1.write_merge(j,j,9,12,'描述:',style_other)
    j+=1
    i=0

# Vertebral anomalies
sheet1.write_merge(31,31,0,2,'              椎体异常',style_top)
sheet1.write_merge(31,31,3,4,'增生退变',style_other)
sheet1.write_merge(31,31,5,12,'其它:',style_other)

# Breast lesions
sheet1.write_merge(32,32,0,2,'              乳腺病变',style_top)
row_rxbb=[u'右侧',u'左侧',u'钙化',u'结节',u'占位']
i,j=0,32
for j in range(32,33):
    sheet1.write_merge(32,32,3,4,'',style_other)
    sheet1.write_merge(32,32,10,12,'描述:',style_other)
    while i<len(row_rxbb):
        sheet1.write(j,i+5,row_rxbb[i],style_other)
        i+=1
    j+=1

# Epigastric lesions
sheet1.write_merge(33,37,0,2,'              上腹部病变',style_top)
column_sfb=[u'肝脏病变',u'肾上腺病变',u'肾脏病变',u'胰腺病变',u'腹腔/腹膜后淋巴结']
i,j=0,33
while i<len(column_sfb):
    sheet1.write_merge(j,j,3,4,column_sfb[i],style_other)
    i+=1
    j+=1
row_sfb_one=[u'无',u'有',u'占位',u'钙化']
i,j=0,33
sheet1.write_merge(j,j,7,10,'蘘肿: 无  有   单发  多发',style_other)
sheet1.write(j,i+5,row_sfb_one[0],style_other)
sheet1.write(j,i+6,row_sfb_one[1],style_other)
sheet1.write(j,i+11,row_sfb_one[2],style_other)
sheet1.write(j,i+12,row_sfb_one[3],style_other)

row_sfb_two=[u'无',u'有',u'右侧',u'左侧',u'增粗',u'占位',u'钙化',u'其它:']
i,j=0,34
while i<len(row_sfb_two):
    sheet1.write(j,i+5,row_sfb_two[i],style_other)
    i+=1
row_sfb_three=[u'无',u'有',u'右侧',u'左侧',u'蘘肿',u'占位',u'萎缩',u'其它:']
i,j=0,35
while i<len(row_sfb_three):
    sheet1.write(j,i+5,row_sfb_three[i],style_other)
    i+=1
row_sfb_four=[u'无',u'有',u'萎缩',u'钙化',u'占位']
i,j=0,36
sheet1.write_merge(j,j,10,12,'描述:',style_other)
while i<len(row_sfb_four):
    sheet1.write(j,i+5,row_sfb_four[i],style_other)
    i+=1
row_sfb_five=[u'无',u'有',u'肿大',u'钙化']
i,j=0,37
sheet1.write_merge(j,j,9,12,'其它:',style_other)
while i<len(row_sfb_five):
    sheet1.write(j,i+5,row_sfb_five[i],style_other)
    i+=1

# Other performance
sheet1.write_merge(38,38,0,2,'               其它表现:',style_top)
sheet1.write_merge(38,38,3,12,'',style_other)

# examination
sheet1.write_merge(39,39,0,2,'              拟诊(可多选)',style_top)
sheet1.write_merge(39,39,3,4,'未见异常',style_other)
sheet1.write(39,5,'炎症',style_other)
sheet1.write_merge(39,39,6,8,'结核:  无  有   活动   非活动',style_other)
sheet1.write(39,9,'肿瘤',style_other)
sheet1.write_merge(39,39,10,12,'其它:',style_other)

# follow-up
sheet1.write_merge(40,41,0,2,'              随诊建议',style_top)
sheet1.write_merge(40,40,3,4,'随诊时间',style_other)
sheet1.write_merge(41,41,3,4,'随诊表现',style_other)
row_sz_one=[u'一个月',u'三个月',u'六个月',u'十二个月']
i,j=0,40
while i<len(row_sz_one):
    sheet1.write(j,i+5,row_sz_one[i],style_other)
    i+=1
sheet1.write_merge(40,40,9,12,'其它建议',style_other)
row_sz_two=[u'',u'',u'',u'',u'',u'',u'',u'']
i,j=0,41
while i<len(row_sz_two):
    sheet1.write(j,i+5,row_sz_two[i],style_other)
    i+=1
w.save('Beijing_Excel.xls')

