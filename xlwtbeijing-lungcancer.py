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
<<<<<<< HEAD
def Excellingcancer(filename,arg):
    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet('CT肺结节结果记录表',cell_overwrite_ok = True)
=======
def Excellingcancer(filename,**arg):
    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet('first',cell_overwrite_ok = True)
>>>>>>> refs/remotes/origin/master

    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1

    alignment=xlwt.Alignment()
    alignment.center=True
    alignment.vert=True
    alignment.horz=2

    fnt_top= Font()
    fnt_top.height=300
    fnt_top.name = u'微软雅黑'
    fnt_top.bold= True
    fnt_other=Font()
    fnt_other.name=u'微软雅黑'
    fnt_left=Font()
    fnt_left.name=u'微软雅黑'
    fnt_left.bold=True
    fnt_colour=Font()
    fnt_colour.name=u'微软雅黑'
    fnt_colour.bold=True
    fnt_colour.colour_index=0x0A


    style_top= XFStyle()
    style_top.font= fnt_top
    style_top.alignment=alignment
    style_top.borders=borders
<<<<<<< HEAD

    style_bottom= XFStyle()
    style_bottom.font= fnt_other
    style_bottom.borders=borders
=======
>>>>>>> refs/remotes/origin/master

    style_other=XFStyle()
    style_other.font=fnt_other
    style_other.alignment=alignment
    style_other.borders=borders

    style_left=XFStyle()
    style_left.font=fnt_left
    style_left.alignment=alignment
    style_left.borders=borders

    style_colour=XFStyle()
    style_colour.font=fnt_colour
    style_colour.alignment=alignment
    style_colour.borders=borders

<<<<<<< HEAD
    NODULE=['Pos','DensityVal','Distance','LongDiameter','ShortDiameter','Smooth','Lobulated','Burr_Depressed','Tractional','Liquefaction','Calc','NoduleIndex','VolumeNo','ReviewTime']
    nodule=[]
    lengthKey=[]
    valueChanged=False
    for key,value in arg.items():
        if key!='Labels':
            if key[1] not in ('LongDiameter','ShortDiameter','Mixed','Solid','Malign','GGO','DensityVal'):
                if key[1] not in ('Smooth','Lobulated','Burr_Depressed','Tractional','Liquefaction','Calc'):
                    if len(value)!=0 :
                        valueChanged=True
                        lengthKey.append(key[0])
                        print 'key[0]',key[0]
                        print 'lengthKey1=',lengthKey
                if key[1] not in ('Pos','Distance','NoduleIndex','VolumeNo','ReviewTime'):
                    if value==1:
                        valueChanged=True
                        lengthKey.append(key[0])
                        print 'lengthKey2=',lengthKey
    lengthKey=list(set(lengthKey))
    lengthKey.sort()
    columnCount=len(lengthKey)
    print 'lengthKey=',lengthKey
    if valueChanged:
        for count in range(len(lengthKey)):
            for content_JJ in NODULE:
                nodule.append((lengthKey[count],content_JJ))
    print 'nodule=',nodule

    if columnCount<=8:
        columnCount=8
=======
    columnCount=0
    for key,value in arg['arg'].items():
        if key=='Labels':
            columnCount=len(value)
    if columnCount<=10:
        columnCount=10
>>>>>>> refs/remotes/origin/master
    sheet1.write_merge(0,1,0,columnCount+3,'北京市肺癌基线调查及早期防治策略研究低剂量螺旋CT结果记录表(肺结节)',style_top)
    sheet1.write_merge(2,2,0,columnCount+3,'ID编号：             姓名：             性别：   男    女                 年龄：                检查日期：        年     月     日',style_left)
    column_left=[u'结节/肿块',u'结节/肿块位置(S肺段)',u'结节密度(实性=1|部分实性=2|非实性=3)',
                 u'结节距离最近胸膜的距离(mm)',u'长径(mm)',u'宽径(mm)',u'边缘光滑',u'边缘分叶',
                 u'毛刺及胸膜凹陷',u'是否牵拉胸膜',u'是否有液化',u'是否含钙化(量<1/2)',
                 u'结节出现序列',u'图像编号',u'建议复查时间',u'专家组会诊意见']
    i,j=0,3
    while i<len(column_left):
        sheet1.write_merge(j,j,0,3,column_left[i],style_left)
<<<<<<< HEAD
        j+=1
        i+=1

    i,j=0,4
    while i<columnCount:
        sheet1.write(3,j,'',style_other)
        j+=1
        i+=1

    col_one=[]
    for count in range(0,len(lengthKey)):
        col_one.append(u'结节%d' %(lengthKey[count]+1))
=======
        j+=1
        i+=1
##    col_one=[u'结节1',u'结节2',u'结节3',u'结节4',u'结节5',u'结节6',
##             u'结节7',u'结节8',u'结节9',u'结节10']
    col_one=[]
    for i in range(1,columnCount+1):
        col_one.append(u'结节%d' %i)
>>>>>>> refs/remotes/origin/master
    i,j=0,4
    while i<len(col_one):
        sheet1.write(3,j,col_one[i],style_other)
        j+=1
        i+=1
<<<<<<< HEAD

##    row_one=[u'',u'',u'',u'',u'',u'Y      N',u'Y      N',u'Y      N',
##                  u'Y      N',u'Y      N',u'Y      N',u'',u'',u'']
    row_one=[u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'']
    i,j=0,4
    for k in range(4,columnCount+4):#len(lengthKey)+4):
=======
    row_one=[u'',u'',u'',u'',u'',u'Y      N',u'Y      N',u'Y      N',
                  u'Y      N',u'Y      N',u'Y      N',u'',u'',u'']
    i,j=0,4
    for k in range(4,columnCount+4):
>>>>>>> refs/remotes/origin/master
        while i<len(row_one):
            sheet1.write(j,k,row_one[i],style_other)
            i+=1
            j+=1
        i,j=0,4
        k+=1
    sheet1.write_merge(18,18,4,columnCount,'',style_other)
    sheet1.write(18,columnCount+1,'填表医师:',style_other)
    sheet1.write_merge(18,18,columnCount+2,columnCount+3,'',style_other)
    sheet1.write_merge(19,19,0,columnCount+3,'注:1.结节内钙化大于病灶1/2的结节不需要填写;'
<<<<<<< HEAD
    '2.结节部位填写:右侧-R,左侧-L表示,后面填写肺段S(1-10),如右上叶尖端为RS1。',style_bottom)

    # Write into Excel
##    print arg['arg']


    for key,value in arg.items():
        for content_nodule in nodule:
            if content_nodule[1] in ('Pos','DensityVal','Distance','LongDiameter','ShortDiameter','NoduleIndex','VolumeNo','ReviewTime') and key==content_nodule:
##                print 'key=',key
                sheet1.write(nodule.index(content_nodule)+4-14*lengthKey.index(content_nodule[0]),lengthKey.index(content_nodule[0])+4,value,style_other)
##                sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,value,style_other)
            if content_nodule[1] in ('Smooth','Lobulated','Burr_Depressed','Tractional','Liquefaction','Calc') and key==content_nodule:
                if value==1:
                    sheet1.write(nodule.index(content_nodule)+4-14*lengthKey.index(content_nodule[0]),lengthKey.index(content_nodule[0])+4,'Y',style_colour)
##                    sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,'Y',style_colour)
                if value==0:
                    sheet1.write(nodule.index(content_nodule)+4-14*lengthKey.index(content_nodule[0]),lengthKey.index(content_nodule[0])+4,'N',style_other)
##                    sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,'N',style_other)

    w.save(filename)
if __name__=='__main__':
    lungNoduleDic= {(0, 'Calc'): 0, 'Labels': [0, 1, 2], (2, 'NoduleIndex'): '', (2, 'Lobulated'): 0, (0, 'Pos'): '', (1, 'Mixed'): 0, (0, 'Smooth'): 0, (1, 'Malign'): 0, (0, 'LongDiameter'): u'4', (2, 'Mixed'): 0, (0, 'Solid'): 0, (0, 'Distance'): '', (1, 'Lobulated'): 1, (2, 'ReviewTime'): ' ', (1, 'Calc'): 0, (1, 'Burr_Depressed'): 0, (0, 'DensityVal'): u'2', (2, 'Malign'): 0, (1, 'Solid'): 0, (2, 'VolumeNo'): '', (2, 'Calc'): 0, (1, 'ReviewTime'): '', (0, 'Liquefaction'): 0, (0, 'NoduleIndex'): '', (2, 'Tractional'): 0, (0, 'Lobulated'): 0, (0, 'GGO'): 0, (0, 'Burr_Depressed'): 0, (2, 'Solid'): 0, (2, 'LongDiameter'): u'6', (2, 'Liquefaction'): 0, (2, 'Distance'): '', (0, 'ShortDiameter'): u'2.2', (2, 'Pos'): '', (2, 'ShortDiameter'): u'3', (2, 'Smooth'): 0, (1, 'NoduleIndex'): '', (1, 'Tractional'): 0, (1, 'DensityVal'): u'1', (0, 'ReviewTime'): '', (1, 'VolumeNo'): '', (1, 'Smooth'): 0, (1, 'GGO'): 0, (1, 'Pos'): '', (0, 'Mixed'): 0, (0, 'Malign'): 0, (1, 'Liquefaction'): 0, (1, 'ShortDiameter'): u'2.6', (2, 'Burr_Depressed'): 0, (2, 'DensityVal'): u'1', (0, 'VolumeNo'): '', (1, 'LongDiameter'): u'6', (0, 'Tractional'): 0, (1, 'Distance'): '', (2, 'GGO'): 0}
    Excellingcancer('Beijing_lungcaner.xls',lungNoduleDic)
=======
    '2.结节部位填写:右侧-R,左侧-L表示,后面填写肺段S(1-10),如右上叶尖端为RS1。',style_other)

    # Write into Excel
##    print arg['arg']
    JJ=['Pos','DensityVal','Distance','LongDiameter','ShortDiameter','Smooth','Lobulated','Burr_Depressed','Tractional','Liquefaction','Calc']
    nodule=[]
    for count in range(columnCount):
        for content_JJ in JJ:
            nodule.append((count,content_JJ))
    for content_nodule in nodule:
        print content_nodule[1]
    for key,value in arg['arg'].items():
        for content_nodule in nodule:
            if content_nodule[1] in ('Pos','DensityVal','Distance','LongDiameter','ShortDiameter') and key==content_nodule:
                sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,value,style_other)
            if content_nodule[1] in ('Smooth','Lobulated','Burr_Depressed','Tractional','Liquefaction','Calc') and key==content_nodule:
                if value==1:
                    sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,'Y',style_colour)
                if value==0:
                    sheet1.write(nodule.index(content_nodule)+4-11*content_nodule[0],content_nodule[0]+4,'N',style_other)

    w.save(filename)
if __name__=='__main__':
    lungNoduleDic={(3, 'DensityVal'): '', (0, 'Calc'): 1, (3, 'Burr_Depressed'): 0, (7, 'Liquefaction'): 0,
     (12, 'Calc'): 0, (10, 'DensityVal'): '', (6, 'Pos'): '', (8, 'ShortDiameter'): u'4.2', (4, 'Lobulated'): 0,
     (6, 'Smooth'): 0, (11, 'Malign'): 0, (9, 'Burr_Depressed'): 1, (14, 'Tractional'): 0, (4, 'Tractional'): 0,
     (3, 'Smooth'): 0, (6, 'Solid'): 0, (0, 'DensityVal'): u'2', (2, 'Malign'): 0, (4, 'Malign'): 0,
     (6, 'Distance'): '', (10, 'Liquefaction'): 0, (6, 'Lobulated'): 0, (14, 'Calc'): 0, (10, 'Calc'): 0,
     (6, 'DensityVal'): '', (3, 'Calc'): 0, (9, 'Smooth'): 0, (9, 'Pos'): '', (10, 'Distance'): '',
     (0, 'Lobulated'): 1, (9, 'Solid'): 0, (11, 'Lobulated'): 0, (5, 'Malign'): 0, (9, 'Tractional'): 0,
     (9, 'LongDiameter'): u'10', (4, 'Burr_Depressed'): 1, (8, 'Malign'): 0, (5, 'Distance'): '',
     (3, 'Liquefaction'): 0, (5, 'Smooth'): 0, 'Labels': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
     (7, 'Mixed'): 0, (10, 'Burr_Depressed'): 0, (13, 'Calc'): 0, (13, 'ShortDiameter'): u'2.4',
     (11, 'Distance'): '', (5, 'GGO'): 0, (14, 'Burr_Depressed'): 0, (9, 'Distance'): '', (4, 'Mixed'): 0,
     (9, 'Malign'): 0, (0, 'Tractional'): 1, (5, 'Tractional'): 0, (12, 'Solid'): 0, (1, 'Mixed'): 0, (1, 'Calc'): 0,
     (9, 'ShortDiameter'): u'3.4', (13, 'Mixed'): 0, (12, 'Pos'): '', (9, 'Lobulated'): 0, (2, 'Lobulated'): 0,
     (7, 'Pos'): '', (0, 'Pos'): u'SR1', (14, 'Mixed'): 0, (4, 'Calc'): 0, (0, 'Smooth'): 1, (10, 'Mixed'): 0,
     (5, 'Liquefaction'): 0, (6, 'Liquefaction'): 0, (0, 'Distance'): u'3', (2, 'ShortDiameter'): u'10',
     (10, 'LongDiameter'): u'8', (1, 'Burr_Depressed'): 0, (9, 'DensityVal'): '', (6, 'LongDiameter'): u'12',
     (13, 'Burr_Depressed'): 1, (13, 'Lobulated'): 0, (11, 'GGO'): 0, (11, 'Tractional'): 0, (7, 'Smooth'): 0,
     (8, 'Solid'): 0, (1, 'ShortDiameter'): u'4', (3, 'GGO'): 0, (2, 'Calc'): 0, (15, 'DensityVal'): u'2',
     (14, 'Malign'): 0, (12, 'LongDiameter'): u'6', (12, 'Mixed'): 0, (7, 'Calc'): 0, (14, 'Liquefaction'): 0,
     (15, 'Distance'): u'2', (15, 'Malign'): 1, (14, 'Lobulated'): 0, (2, 'Pos'): '', (5, 'DensityVal'): '',
     (13, 'Malign'): 0, (2, 'Liquefaction'): 0, (13, 'Solid'): 0, (1, 'Tractional'): 0, (7, 'Tractional'): 0,
     (11, 'LongDiameter'): u'6', (15, 'Smooth'): 1, (4, 'Pos'): '', (12, 'DensityVal'): '', (6, 'Malign'): 0,
     (8, 'Pos'): '', (1, 'Liquefaction'): 0, (4, 'GGO'): 0, (5, 'LongDiameter'): u'6', (13, 'Distance'): '',
     (10, 'Solid'): 0, (4, 'Smooth'): 1, (2, 'Burr_Depressed'): 0, (5, 'Calc'): 0, (2, 'DensityVal'): '',
     (12, 'GGO'): 0, (4, 'Distance'): '', (2, 'Smooth'): 0, (10, 'ShortDiameter'): u'2.4', (11, 'Pos'): '',
     (7, 'Lobulated'): 0, (13, 'GGO'): 0, (12, 'Lobulated'): 0, (5, 'Mixed'): 0, (10, 'Malign'): 0,
     (15, 'LongDiameter'): u'5', (8, 'Liquefaction'): 0, (3, 'ShortDiameter'): u'6.8', (2, 'Mixed'): 0,
     (14, 'ShortDiameter'): u'2', (15, 'Mixed'): 0, (1, 'Smooth'): 0, (14, 'Smooth'): 0, (10, 'Pos'): '',
     (3, 'Distance'): '', (8, 'Lobulated'): 0, (5, 'Pos'): '', (3, 'Malign'): 0, (3, 'Lobulated'): 0,
     (3, 'Solid'): 0, (5, 'Burr_Depressed'): 0, (1, 'Solid'): 0, (3, 'Tractional'): 0, (10, 'Tractional'): 0,
     (13, 'LongDiameter'): u'6', (7, 'ShortDiameter'): u'3.8', (8, 'DensityVal'): '', (2, 'GGO'): 0,
     (8, 'Burr_Depressed'): 0, (15, 'Liquefaction'): 1, (4, 'ShortDiameter'): u'5', (7, 'GGO'): 0,(0, 'Malign'): 1,
     (12, 'Malign'): 0, (12, 'Smooth'): 0, (13, 'Liquefaction'): 0, (14, 'Pos'): '',(14, 'DensityVal'): '',
     (11, 'Mixed'): 0, (0, 'Liquefaction'): 1, (5, 'Solid'): 0, (8, 'Mixed'): 0,(13, 'DensityVal'): '',
     (6, 'Tractional'): 0, (4, 'DensityVal'): '', (3, 'Pos'): '', (3, 'LongDiameter'): u'20', (14, 'Solid'): 0,
     (5, 'ShortDiameter'): u'2.2', (10, 'Lobulated'): 0, (15, 'Tractional'): 1, (5, 'Lobulated'): 0, (6, 'Calc'): 0,
     (11, 'DensityVal'): '', (8, 'Calc'): 0, (11, 'Burr_Depressed'): 0, (14, 'Distance'): '', (15, 'Calc'): 1,
     (15, 'Solid'): 0, (7, 'Distance'): '', (15, 'Lobulated'): 1, (1, 'DensityVal'): '', (1, 'Malign'): 0,
     (0, 'LongDiameter'): u'24', (14, 'GGO'): 0, (8, 'Distance'): '', (12, 'Tractional'): 0, (12, 'Distance'): '',
     (0, 'Solid'): 1, (11, 'Smooth'): 0, (11, 'ShortDiameter'): u'3.8', (0, 'GGO'): 0, (1, 'Lobulated'): 0,
     (15, 'Pos'): u'SR1', (7, 'DensityVal'): '', (8, 'Smooth'): 0, (11, 'Liquefaction'): 0, (15, 'Burr_Depressed'): 1,
     (6, 'Burr_Depressed'): 0, (7, 'Burr_Depressed'): 0, (11, 'Calc'): 0, (10, 'GGO'): 0, (6, 'GGO'): 0,
     (7, 'Solid'): 0, (4, 'LongDiameter'): u'16', (14, 'LongDiameter'): u'4', (9, 'GGO'): 0, (2, 'Tractional'): 0,
     (12, 'Liquefaction'): 0, (4, 'Solid'): 0, (0, 'Burr_Depressed'): 1, (2, 'Solid'): 0, (9, 'Liquefaction'): 0,
     (12, 'Burr_Depressed'): 0, (12, 'ShortDiameter'): u'3.6', (2, 'Distance'): '', (2, 'LongDiameter'): u'20',
     (0, 'ShortDiameter'): u'8.8', (15, 'ShortDiameter'): u'6', (4, 'Liquefaction'): 0, (6, 'Mixed'): 0,
     (3, 'Mixed'): 0, (13, 'Smooth'): 0, (9, 'Calc'): 0, (13, 'Pos'): '', (6, 'ShortDiameter'): u'5', (1, 'GGO'): 0,
     (1, 'Pos'): '', (8, 'LongDiameter'): u'10', (0, 'Mixed'): 0, (10, 'Smooth'): 0, (7, 'Malign'): 0, (8, 'GGO'): 0,
     (11, 'Solid'): 0, (8, 'Tractional'): 0, (13, 'Tractional'): 0, (7, 'LongDiameter'): u'14', (9, 'Mixed'): 0,
     (1, 'LongDiameter'): u'8', (1, 'Distance'): '', (15, 'GGO'): 1}
    Excellingcancer('Beijing_lungcaner.xls',arg=lungNoduleDic)
>>>>>>> refs/remotes/origin/master


