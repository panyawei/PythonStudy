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
def Excellingcancer(filename,arg):
    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet('CT肺结节结果记录表',cell_overwrite_ok = True)

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

    style_bottom= XFStyle()
    style_bottom.font= fnt_other
    style_bottom.borders=borders

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
    sheet1.write_merge(0,1,0,columnCount+3,'北京市肺癌基线调查及早期防治策略研究低剂量螺旋CT结果记录表(肺结节)',style_top)
    sheet1.write_merge(2,2,0,columnCount+3,'ID编号：             姓名：             性别：   男    女                 年龄：                检查日期：        年     月     日',style_left)
    column_left=[u'结节/肿块',u'结节/肿块位置(S肺段)',u'结节密度(实性=1|部分实性=2|非实性=3)',
                 u'结节距离最近胸膜的距离(mm)',u'长径(mm)',u'宽径(mm)',u'边缘光滑',u'边缘分叶',
                 u'毛刺及胸膜凹陷',u'是否牵拉胸膜',u'是否有液化',u'是否含钙化(量<1/2)',
                 u'结节出现序列',u'图像编号',u'建议复查时间',u'专家组会诊意见']
    i,j=0,3
    while i<len(column_left):
        sheet1.write_merge(j,j,0,3,column_left[i],style_left)
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
    i,j=0,4
    while i<len(col_one):
        sheet1.write(3,j,col_one[i],style_other)
        j+=1
        i+=1

##    row_one=[u'',u'',u'',u'',u'',u'Y      N',u'Y      N',u'Y      N',
##                  u'Y      N',u'Y      N',u'Y      N',u'',u'',u'']
    row_one=[u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'']
    i,j=0,4
    for k in range(4,columnCount+4):#len(lengthKey)+4):
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


