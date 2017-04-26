# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        generateResultFile.py
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     10/02/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlwt #exampleB
from xlwt import *
##class xlwtExcel:
def ExcelXlwt(filename,**args):

    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet(u'CT结果记录表',cell_overwrite_ok = True)
##    sheet1.wnd_visible=True
    borders=xlwt.Borders()
    borders.left=1
    borders.right=1
    borders.top=1
    borders.bottom=1
    alignment=xlwt.Alignment()
    alignment.center=True
    alignment.vert=True
    alignment.horz=2

    fnt=Font()
    fnt.name = u'微软雅黑'
    fnt.bold= True
    fnt.height=300
    fnt_top= Font()
    fnt_top.name = u'微软雅黑'
    fnt_top.bold= True
    fnt_other=Font()
    fnt_other.name=u'微软雅黑'
    fnt_other_other=Font()
    fnt_other_other.name=u'微软雅黑'

    style=XFStyle()
    style_top= XFStyle()
    style_other=XFStyle()
    style_other_other=XFStyle()

    style.font=fnt
    style.borders=borders
    style.alignment=alignment

    style_top.font= fnt_top
    style_top.alignment=alignment
    style_top.borders=borders

    style_other.font=fnt_other
    style_other.alignment=alignment
    style_other.borders=borders

    style_other_other.font=fnt_other_other
    style_other_other.borders=borders

    sheet1.write_merge(0,0,0,11,'北京市肺癌基线调查及早期防治策略研究低剂量螺旋CT结果记录表',style)
    sheet1.write_merge(1,1,0,11,'(是否需要专家组会诊?  是      否        )',style_other)
    # 肺实质/气管/支气管异常
    sheet1.write_merge(2,2,0,11,'ID编号：                  姓名：               性别：    男      女          年龄：          检查日期：       年    月    日',style_top)
    sheet1.write_merge(3,13,0,2,'肺实质/气管/支气管异常',style_top)
    sheet1.write_merge(3,4,3,5,'病变/部位',style_other)
    sheet1.write_merge(3,3,6,8,'右侧(RS1-10)',style_other)
    sheet1.write_merge(3,3,9,11,'左侧(LS1-10)',style_other)
    sheet1.write(4,6,'上',style_other)
    sheet1.write(4,7,'中',style_other)
    sheet1.write(4,8,'下',style_other)
    sheet1.write(4,9,'上',style_other)
    sheet1.write(4,10,'舌',style_other)
    sheet1.write(4,11,'下',style_other)
    sheet1.write_merge(5,5,3,4,'肺实质/GGO',style_other)

    row_column=[u'',u'',u'',u'',u'',u'']
    i,j=0,5

    for j in range(5,13):
        while i<len(row_column) and j!=12:
            sheet1.write(j,i+6,row_column[i],style_other)
            i+=1
        i=0
##    ####
    for j in range(5,12):
        sheet1.write(j,5,'无/有',style_other)

    sheet1.write(13,5,'无/有',style_other)
##
    sheet1.write_merge(6,6,3,4,'树芽征/腺泡结节',style_other)
    sheet1.write_merge(7,7,3,4,'纤维瘢痕/梗结',style_other)
    sheet1.write_merge(8,8,3,4,'支气管扩张',style_other)
    sheet1.write_merge(9,9,3,4,'肺间质纤维化',style_other)
    sheet1.write_merge(10,10,3,4,'肺不张',style_other)
    sheet1.write_merge(11,11,3,4,'肺气肿',style_other)
    sheet1.write_merge(12,12,3,4,'附加描述:',style_other)
    sheet1.write_merge(12,12,5,11,'',style_other)
    sheet1.write_merge(13,13,3,4,'气管/支气管',style_other)
    sheet1.write(13,6,'结节',style_other)
    sheet1.write_merge(13,13,7,8,'管壁增厚',style_other)
    sheet1.write(13,9,'腔狭窄',style_other)
    sheet1.write(13,10,'部位:',style_other)
    sheet1.write(13,11,'',style_other)

    #  胸腔/胸膜异常
    sheet1.write_merge(14,16,0,2,'胸腔/胸膜异常',style_top)
##    column_chest=['胸膜积液','胸膜增厚','胸膜斑']
##    column_chest=['XMJY','XMZH','XMB']
    column_chest=['胸膜积液','胸膜增厚','胸膜斑']
    i,j=0,14
    while i<len(column_chest):
        sheet1.write_merge(j,j,3,4,column_chest[i],style_other)
        j+=1
        i+=1
##    row_chest_one=['ZC','YC','SC','SL','ZL','DL']
    row_chest_one=[u'右侧',u'左侧',u'双侧',u'少量',u'中量',u'大量']
    i,j=0,14
    while i<len(row_chest_one):
        sheet1.write(j,i+6,row_chest_one[i],style_other)
        i+=1
##    row_chest_two=['ZC','YC','SC','JX','GF','GH']
    row_chest_two=[u'右侧',u'左侧',u'双侧',u'局限',u'广泛',u'钙化']
    i,j=0,15
    while i<len(row_chest_two):
        sheet1.write(j,i+6,row_chest_two[i],style_other)
        i+=1
    sheet1.write(14,5,'无/有',style_other)
    sheet1.write(15,5,'无/有',style_other)
    sheet1.write(16,5,'无/有',style_other)
    sheet1.write_merge(16,16,6,7,'胸膜病变补充:',style_other_other)
    sheet1.write_merge(16,16,8,11,'',style_other_other)

    # 心脏/大血管
    sheet1.write_merge(17,22,0,2,'心脏/大血管',style_top)
    column_bloodvessel=['冠状动脉钙化','心包增厚','心包积液','心影增大','主动脉病变','肺动脉异常']
    i,j=0,17
    while i<len(column_bloodvessel):
        sheet1.write_merge(j,j,3,4,column_bloodvessel[i],style_other)
        i+=1
        j+=1

    for j in range(17,23):
        sheet1.write(j,5,'无/有',style_other)

    row_bloodvessel_one=['左主干','前降支','左旋支','右主干','','']
    i,j=0,17
    while i<len(row_bloodvessel_one):
        sheet1.write(j,i+6,row_bloodvessel_one[i],style_other)
        i+=1

    row_bloodvessel_two=['局限','弥漫']
    i,j=0,18
    while i<len(row_bloodvessel_two):
        sheet1.write(j,i+6,row_bloodvessel_two[i],style_other)
        i+=1
    sheet1.write(18,8,'其它:',style_other)
    sheet1.write_merge(18,18,9,11,'',style_other_other)
    row_bloodvessel_three=['局限','弥漫','少量','中量','大量','']
    i,j=0,19
    while i<len(row_bloodvessel_three):
        sheet1.write(j,i+6,row_bloodvessel_three[i],style_other)
        i+=1
##    sheet1.write_merge(19,19,8,11,'少量           中量          大量',style_other)
    row_bloodvessel_four=['左心室','右心室','左心房','右心房','普大','其它:']
    i,j=0,20
    while i<len(row_bloodvessel_four):
        sheet1.write(j,i+6,row_bloodvessel_four[i],style_other)
        i+=1
    row_bloodvessel_five=['壁钙化','动脉瘤']
    i,j=0,21
    while i<len(row_bloodvessel_five):
        sheet1.write(j,i+6,row_bloodvessel_five[i],style_other)
        i+=1
    sheet1.write(21,8,'其它:',style_other)
    sheet1.write_merge(21,21,9,11,'',style_other_other)
    row_bloodvessel_six=['右PA','左PA']
    i,j=0,22
    while i<len(row_bloodvessel_six):
        sheet1.write(j,i+6,row_bloodvessel_six[i],style_other)
        i+=1
    sheet1.write(22,8,'描述:',style_other)
    sheet1.write_merge(22,22,9,11,'',style_other_other)

    # lymph gland
    sheet1.write_merge(23,25,0,2,'纵隔/肺门/其他部位淋巴结',style_top)
    column_lbj=['淋巴结>=1cm','淋巴结<1cm','淋巴结钙化']
    i,j=0,23
    while i<len(column_lbj):
        sheet1.write_merge(j,j,3,4,column_lbj[i],style_other)
        i+=1
        j+=1

    for j in range(23,26):
        sheet1.write(j,5,'无/有',style_other)

    j=23
    for j in range(23,26):
        sheet1.write(j,6,'部位:',style_other)
        sheet1.write_merge(j,j,7,11,'',style_other)

    # mediastinumLesion
    sheet1.write_merge(26,29,0,2,'纵隔病变',style_top)
    column_zgbb=['纵隔占位','食道病变','甲状腺病变']
    i,j=0,26
    while i<len(column_zgbb):
        sheet1.write_merge(j,j,3,4,column_zgbb[i],style_other)
        i+=1
        j+=1
    sheet1.write_merge(29,29,3,4,'附加描述:',style_other)
    sheet1.write_merge(29,29,5,11,'',style_other_other)
    for j in range(26,29):
        sheet1.write(j,5,'无/有',style_other)

    sheet1.write_merge(26,26,6,7,'部位及描述:',style_other)
    sheet1.write_merge(26,26,8,11,'',style_other_other)
    row_zgbb_two=['上段','中段','下端','补充:']
    i,j=0,27
    while i<len(row_zgbb_two):
        sheet1.write(j,i+6,row_zgbb_two[i],style_other)
        i+=1
    sheet1.write_merge(27,27,10,11,'',style_other_other)
    row_zgbb_three=['左叶','右叶','弥漫','实性','蘘性','其它:']
    i,j=0,28
    while i<len(row_zgbb_three):
        sheet1.write(j,i+6,row_zgbb_three[i],style_other)
        i+=1

    # Chest wall lesion
    sheet1.write_merge(30,32,0,2,'胸壁病变',style_top)
    sheet1.write_merge(30,30,3,4,'胸壁软组织',style_other)
    sheet1.write_merge(31,31,3,4,'肋骨异常',style_other)
    sheet1.write_merge(32,32,3,4,'附加描述:',style_other)
    sheet1.write_merge(32,32,5,11,'',style_other_other)

    for j in range(30,32):
        sheet1.write(j,5,'无/有',style_other)
    row_xbbb=['右侧','左侧']
    i,j=0,30
    for j in range(30,32):
        while i<len(row_xbbb):
            sheet1.write(j,i+6,row_xbbb[i],style_other)
            i+=1
        sheet1.write(j,8,'描述:',style_other)
        sheet1.write_merge(j,j,9,11,'',style_other_other)
        i=0

    # Vertebral anomalies
    sheet1.write_merge(33,33,0,2,'椎体异常',style_top)
    sheet1.write_merge(33,33,3,4,'增生退变',style_other)
    sheet1.write(33,5,'其它:',style_other)
    sheet1.write_merge(33,33,6,11,'',style_other_other)

    # Breast lesions
    sheet1.write_merge(34,34,0,2,'乳腺病变',style_top)
    row_rxbb=['右侧','左侧','钙化','结节','占位']
    i,j=0,34
    for j in range(34,35):
        sheet1.write_merge(34,34,3,4,'',style_other)
        sheet1.write(34,10,'描述:',style_other)
        sheet1.write(34,11,'',style_other)
        while i<len(row_rxbb):
            sheet1.write(j,i+5,row_rxbb[i],style_other)
            i+=1
        j+=1

    # Epigastric lesions
    sheet1.write_merge(35,39,0,2,'上腹部病变',style_top)
    column_sfb=['肝脏病变','肾上腺病变','肾脏病变','胰腺病变','腹腔/腹膜后淋巴结']
    i,j=0,35
    while i<len(column_sfb):
        sheet1.write_merge(j,j,3,4,column_sfb[i],style_other)
        i+=1
        j+=1
    for j in range(35,40):
        sheet1.write(j,5,'无/有',style_other)
    row_sfb_one=['占位','钙化']
    i,j=0,35
    sheet1.write_merge(j,j,6,9,'蘘肿:    无       有      单发     多发',style_other)
    sheet1.write(j,i+10,row_sfb_one[0],style_other)
    sheet1.write(j,i+11,row_sfb_one[1],style_other)

    row_sfb_two=['右侧','左侧','增粗','占位','钙化','其它:']
    i,j=0,36
    while i<len(row_sfb_two):
        sheet1.write(j,i+6,row_sfb_two[i],style_other)
        i+=1
    row_sfb_three=['右侧','左侧','蘘肿','占位','萎缩','其它:']
    i,j=0,37
    while i<len(row_sfb_three):
        sheet1.write(j,i+6,row_sfb_three[i],style_other)
        i+=1
    row_sfb_four=['萎缩','钙化','占位']
    i,j=0,38
    sheet1.write(j,9,'描述:',style_other)
    sheet1.write_merge(j,j,10,11,'',style_other_other)
    while i<len(row_sfb_four):
        sheet1.write(j,i+6,row_sfb_four[i],style_other)
        i+=1
    row_sfb_five=['肿大','钙化']
    i,j=0,39
    sheet1.write(j,8,'其它:',style_other)
    sheet1.write_merge(j,j,9,11,'',style_other_other)
    while i<len(row_sfb_five):
        sheet1.write(j,i+6,row_sfb_five[i],style_other)
        i+=1


    # Other performance
    sheet1.write_merge(40,40,0,2,'其它表现:',style_top)
    sheet1.write_merge(40,40,3,11,'',style_other)

    # examination
    sheet1.write_merge(41,41,0,2,'拟诊(可多选)',style_top)
    sheet1.write_merge(41,41,3,4,'未见异常',style_other)
    sheet1.write(41,5,'炎症',style_other)
    sheet1.write_merge(41,41,6,8,'结核:    无    有    活动    非活动',style_other)
    sheet1.write(41,9,'肿瘤',style_other)
    sheet1.write(41,10,'其它:',style_other)
    sheet1.write(41,11,'',style_other_other)

    # follow-up
    sheet1.write_merge(42,43,0,2,'随诊建议',style_top)
    sheet1.write_merge(42,42,3,4,'随诊时间',style_other)
    sheet1.write_merge(43,43,3,4,'随诊表现',style_other)
    row_sz_one=['一个月','三个月','六个月','十二个月']
    i,j=0,42
    while i<len(row_sz_one):
        sheet1.write(j,i+5,row_sz_one[i],style_other)
        i+=1
    sheet1.write(42,9,'其它建议:',style_other)
    sheet1.write_merge(42,42,10,11,'',style_other_other)
    sheet1.write_merge(43,43,5,11,'',style_other_other)

    sheet1.write_merge(44,45,0,2,'专家会诊意见及填表医生',style_top)
    sheet1.write_merge(44,45,3,11,'',style_other)

    #  write into Excel
    dic=args
    print 'dic=',dic
    table1Items=('FSZ_GGO','SYZ_XPJJ','XWBH_JG','ZQGKZ','FJZXWH','FBZ','FQZ','FJMS','QG_ZQG')
    for key,value in dic['arg'][0].items():
        rowIndex1=table1Items.index(key)+5
        if key in table1Items:
            if len(value)!=0:
                sheet1.write(rowIndex1,5,'有',style_other)
                for val in value:
                    if(len(val)==2):
                        if val[1]==0:
                            sheet1.write(rowIndex1,val[1]+5,'有',style_other)
                        if 5<=rowIndex1 <12 and val[1]>0:
                            sheet1.write(rowIndex1,val[1]+5,'✔',style_other)
                        if(rowIndex1==12):
                            sheet1.write(rowIndex1,5,val,style_other)
                        if(rowIndex1==13):
                            if (len(val)==2 and val[1]>0):
                                if val[1]==1:
                                    sheet1.write(rowIndex1,6,u'结节 ✔',style_other)
                                elif val[1]==2:
                                    sheet1.write_merge(rowIndex1,rowIndex1,7,8,u'管壁增厚 ✔',style_other)
                                elif val[1]==3:
                                    sheet1.write(rowIndex1,9,u'腔狭窄 ✔',style_other)
                                else:
                                    sheet1.write(rowIndex1,11,val,style_other)
                        if val[1]==0 and rowIndex1==13:
                            sheet1.write(table1Items.index(key)+5,5,'有',style_other)
                    else:
                        if(rowIndex1==12):
                            sheet1.write(rowIndex1,5,val,style_other)
                        if(rowIndex1==13):
                            sheet1.write(rowIndex1,11,val,style_other)
            else:
                if (rowIndex1!=12):
                    sheet1.write(table1Items.index(key)+5,5,'无',style_other)

    table2Items=('XQJY','XMZH','XMB')
    for key,value in dic['arg'][1].items():
        if key in table2Items:
            if len(value)!=0:
                rowIndex2=table2Items.index(key)
                for val in value:
                    if rowIndex2==0 or rowIndex2==1:
                        if val[1]>=1:
                            sheet1.write(table2Items.index(key)+14,5,'有',style_other)
                        else:
                            sheet1.write(table2Items.index(key)+14,5,'无',style_other)
                    if len(val)==2:
                        if rowIndex2==0 and val[1]>1:
                            sheet1.write(14,val[1]+4,row_chest_one[val[1]-2]+u' ✔' ,style_other)
                        if rowIndex2==1 and val[1]>1:
                            sheet1.write(15,val[1]+4,row_chest_two[val[1]-2]+u' ✔' ,style_other)
                    if rowIndex2==2:
                        if len(val)==2:
                            if val[1]==1:
                                sheet1.write(table2Items.index(key)+14,5,'有',style_other)
                            elif val[1]==0:
                                sheet1.write(table2Items.index(key)+14,5,'无',style_other)
                            else:
                                sheet1.write(16,8,val,style_other)
                                sheet1.write(table2Items.index(key)+14,5,'有',style_other)
                        else:
                            sheet1.write(16,8,val,style_other)
                            sheet1.write(table2Items.index(key)+14,5,'有',style_other)
            else:
                sheet1.write(table2Items.index(key)+14,5,'无',style_other)


    table3Items=('GZDMGH','XBZH','XBJY','XYZD','ZDMBB','FDMYC')
    for key,value in dic['arg'][2].items():
        if key in table3Items:
            if len(value)!=0:
                rowIndex3=table3Items.index(key)
                for val in value:
                    if isinstance(val,tuple):
                        if val[1]>=1:
                            sheet1.write(table3Items.index(key)+17,5,'有',style_other)
                        else:
                            sheet1.write(table3Items.index(key)+17,5,'无',style_other)
                    if len(val)==2:
                        if val[1]>=2:
                            if isinstance(val,tuple):
                                row_bloodvessel=row_bloodvessel_one,row_bloodvessel_two,row_bloodvessel_three,row_bloodvessel_four,row_bloodvessel_five,row_bloodvessel_six
                                sheet1.write(rowIndex3+17,val[1]+4,row_bloodvessel[rowIndex3][val[1]-2]+' ✔',style_other)
                            if isinstance(val,unicode):
                                if rowIndex3==1 or rowIndex3==4 or rowIndex3==5:
                                    sheet1.write(rowIndex3+17,9,val,style_other)
                                    sheet1.write(table3Items.index(key)+17,5,'有',style_other)
                                if rowIndex3==3:
                                    sheet1.write(rowIndex3+17,11,u'其它:'+val,style_other_other)
                                    sheet1.write(table3Items.index(key)+17,5,'有',style_other)
                    else:
                        if rowIndex3==1 or rowIndex3==4 or rowIndex3==5:
                            sheet1.write(rowIndex3+17,9,val,style_other)
                            sheet1.write(table3Items.index(key)+17,5,'有',style_other)
                        if rowIndex3==3:
                            sheet1.write(rowIndex3+17,11,u'其它:'+val,style_other_other)
                            sheet1.write(table3Items.index(key)+17,5,'有',style_other)
            else:
                sheet1.write(table3Items.index(key)+17,5,'无',style_other)

    table4Items=('LBJD','LBJX','LBJGH')
    for key,value in dic['arg'][3].items():
        if key in table4Items:
            if (len(value)!=0):
                rowIndex4=table4Items.index(key)+23
                for val in value:
                    if len(val)==2:
                        if val[1]==1:
                            sheet1.write(rowIndex4,5,'有',style_other)
                        if val[1]==0:
                            sheet1.write(rowIndex4,5,'无',style_other)
                        if val[1]>1:
                            sheet1.write(rowIndex4,5,'有',style_other)
                            sheet1.write(rowIndex4,7,val,style_other)
                    else:
                        sheet1.write(rowIndex4,5,'有',style_other)
                        sheet1.write(rowIndex4,7,val,style_other)
            else:
                sheet1.write(table4Items.index(key)+23,5,'无',style_other)

    table5Items=('ZGZW','SDBB','JZXBB','FJMS')
    for key,value in dic['arg'][4].items():
        if key in table5Items:
            rowIndex5=table5Items.index(key)
            if len(value)!=0:
                for val in value:
                    if isinstance(val,tuple):
                        if val[1]>=1:
                            sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                        if val[1]==0:
                            sheet1.write(table5Items.index(key)+26,5,'无',style_other)
                    if len(val)==2:
                        if key=='ZGZW':
                            if isinstance(val,tuple):
                                if val[1]==1:
                                    sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                                if val[1]==0:
                                    sheet1.write(table5Items.index(key)+26,5,'无',style_other)
                            if isinstance(val,unicode):
                                sheet1.write(26,5,'有',style_other)
                                sheet1.write(rowIndex5+26,8,val,style_other)

                        if key=='SDBB':
                            if isinstance(val,tuple):
                                if 4>=val[1]>=2:
                                    sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                                    sheet1.write(rowIndex5+26,val[1]+4,row_zgbb_two[val[1]-2]+' ✔',style_other)
                                if val[1]==0:
                                    sheet1.write(table5Items.index(key)+26,5,'无',style_other)
                            if isinstance(val,unicode):
                                sheet1.write(rowIndex5+26,10,val,style_other)
                                sheet1.write(27,5,'有',style_other)
                        if key=='JZXBB':
                            if isinstance(val,tuple):
                                if 6>=val[1]>=2:
                                    sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                                    sheet1.write(rowIndex5+26,val[1]+4,row_zgbb_three[val[1]-2]+' ✔',style_other)
                                if val[1]==0:
                                    sheet1.write(table5Items.index(key)+26,5,'无',style_other)
                            if isinstance(val,unicode):
                                sheet1.write(rowIndex5+26,11,u'其它:'+val,style_other_other)
                                sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                        if key=='FJMS':
                            if isinstance(val,unicode):
                                sheet1.write(rowIndex5+26,5,val,style_other)
                    else:
                        if rowIndex5==0:
                            sheet1.write(rowIndex5+26,8,val,style_other)
                            sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                        if rowIndex5==3:
                            sheet1.write(rowIndex5+26,5,val,style_other)
                            sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                        if rowIndex5==1:
                            sheet1.write(rowIndex5+26,10,val,style_other)
                            sheet1.write(table5Items.index(key)+26,5,'有',style_other)
                        if rowIndex5==2:
                            sheet1.write(rowIndex5+26,11,u'其它:'+val,style_other_other)
                            sheet1.write(table5Items.index(key)+26,5,'有',style_other)
            else:
                if rowIndex5!=3:
                    sheet1.write(table5Items.index(key)+26,5,'无',style_other)

    table6Items=('XMRZZ','LGYC','FJMS')
    for key,value in dic['arg'][5].items():
        if key in table6Items:
            rowIndex6=table6Items.index(key)
            if len(value)!=0:
                for val in value:
                    if rowIndex6==0 or rowIndex6==1:
                        if isinstance(val,tuple):
                            if val[1]>=1:
                                sheet1.write(table6Items.index(key)+30,5,'有',style_other)
                            else:
                                sheet1.write(table6Items.index(key)+30,5,'无',style_other)
                    if len(val)==2:
                        if key=='XMRZZ' or key=='LGYC':
                            if isinstance(val,tuple):
                                sheet1.write(rowIndex6+30,val[1]+4,row_xbbb[val[1]-2]+' ✔',style_other)
                            if isinstance(val,unicode):
                                if rowIndex6==0:
                                    sheet1.write(rowIndex6+30,9,val,style_other)
                                    sheet1.write(table6Items.index(key)+30,5,'有',style_other)
                                if rowIndex6==1:
                                    sheet1.write(rowIndex6+30,9,val,style_other)
                                    sheet1.write(table6Items.index(key)+30,5,'有',style_other)
                        if rowIndex6==2:sheet1.write(rowIndex6+30,5,val,style_other)
                    else:
                        if rowIndex6==0:
                            sheet1.write(rowIndex6+30,9,val,style_other)
                            sheet1.write(table6Items.index(key)+30,5,'有',style_other)
                        if rowIndex6==1:
                            sheet1.write(rowIndex6+30,9,val,style_other)
                            sheet1.write(table6Items.index(key)+30,5,'有',style_other)
                        if rowIndex6==2:sheet1.write(rowIndex6+30,5,val,style_other)
            else:
                if rowIndex6!=2:
                    sheet1.write(table6Items.index(key)+30,5,'无',style_other)

    table7Items=('ZSTB',)
    for key,value in dic['arg'][6].items():
        if key in table7Items:
            rowIndex7=table7Items.index(key)
            if len(value)!=0:
                for val in value:
                    if len(val)==2:
                        if isinstance(val,tuple):
                            sheet1.write(rowIndex7+33,3,'增生退变 ✔',style_other)
                        if isinstance(val,unicode):
                            sheet1.write(rowIndex7+33,6,val,style_other)
                    else:
                        sheet1.write(rowIndex7+33,6,val,style_other)

    table8Items=('RXBB',)
    for key,value in dic['arg'][7].items():
        if key in table8Items:
            rowIndex8=table8Items.index(key)
            if len(value)!=0:
                for val in value:
                    if len(val)==2:
                        if isinstance(val,tuple):
                            sheet1.write(rowIndex8+34,val[1]+5,row_rxbb[val[1]]+'✔',style_other)
                        if isinstance(val,unicode):
                            sheet1.write(rowIndex8+34,11,val,style_other)
                    else:
                        sheet1.write(rowIndex8+34,11,val,style_other)

    table9Items=('GZBB','SSXBB','SZBB','YXBB','FQFM_HLBJ')
    for key,value in dic['arg'][8].items():
        if key in table9Items:
            rowIndex9=table9Items.index(key)
            if len(value)!=0:
                for val in value:
                    if isinstance(val,tuple):
                        if val[1]>=1:
                            sheet1.write(rowIndex9+35,5,'有',style_other)
                            if rowIndex9==0 and val[1]==3:
                                sheet1.write(rowIndex9+35,5,'无',style_other)
                        else:
                            sheet1.write(rowIndex9+35,5,'无',style_other)
                    if len(val)==2:
                        if isinstance(val,tuple):
                            if key=='GZBB':
                                if val[1]==3:
                                    sheet1.write(rowIndex9+35,6,'蘘肿:    无 ✔      有      单发     多发',style_other)
                                if val[1]==4:
                                    sheet1.write(rowIndex9+35,6,'蘘肿:    无       有 ✔     单发     多发',style_other)
                                if val[1]==5:
                                    sheet1.write(rowIndex9+35,6,'蘘肿:    无       有 ✔     单发 ✔    多发',style_other)
                                if val[1]==6:
                                    sheet1.write(rowIndex9+35,6,'蘘肿:    无       有 ✔     单发     多发✔',style_other)
                                if val[1]==7 or val[1]==8:
                                    sheet1.write(rowIndex9+35,val[1]+3,row_sfb_one[val[1]-7]+'✔',style_other)
                            elif val[1]>1:
                                row_sfb=row_sfb_one,row_sfb_two,row_sfb_three,row_sfb_four,row_sfb_five
                                sheet1.write(rowIndex9+35,val[1]+4,row_sfb[rowIndex9][val[1]-2]+'✔',style_other)
                        if isinstance(val,unicode):
                            if rowIndex9==1 :
                                sheet1.write(rowIndex9+35,11,u'其它:'+val,style_other)
                                sheet1.write(rowIndex9+35,5,'有',style_other)
                            if rowIndex9==2 :
                                sheet1.write(rowIndex9+35,11,u'其它:'+val,style_other)
                                sheet1.write(rowIndex9+35,5,'有',style_other)
                            if rowIndex9==3 :
                                sheet1.write(rowIndex9+35,10,val,style_other)
                                sheet1.write(rowIndex9+35,5,'有',style_other)
                            if rowIndex9==4 :
                                sheet1.write(rowIndex9+35,9,val,style_other)
                                sheet1.write(rowIndex9+35,5,'有',style_other)
                    else:
                        if rowIndex9==1 :
                            sheet1.write(rowIndex9+35,11,u'其它:'+val,style_other)
                            sheet1.write(rowIndex9+35,5,'有',style_other)
                        if rowIndex9==2 :
                            sheet1.write(rowIndex9+35,11,u'其它:'+val,style_other)
                            sheet1.write(rowIndex9+35,5,'有',style_other)
                        if rowIndex9==3 :
                            sheet1.write(rowIndex9+35,10,val,style_other)
                            sheet1.write(rowIndex9+35,5,'有',style_other)
                        if rowIndex9==4 :
                            sheet1.write(rowIndex9+35,9,val,style_other)
                            sheet1.write(rowIndex9+35,5,'有',style_other)
            else:
                sheet1.write(rowIndex9+35,5,'无',style_other)

    table10Items=('QTBX',)
    for key,value in dic['arg'][9].items():
        for val in value:
            if key=='QTBX':
                sheet1.write(40,3,val,style_other)

    table11Items=('NIZHEN',)
    for key,value in dic['arg'][10].items():
        if key in table11Items:
            rowIndex11=table11Items.index(key)
            if len(value)!=0:
                for val in value:
                    if len(val)==2:
                        if isinstance(val,tuple):
                            if val[1]==0:
                                sheet1.write(rowIndex11+41,val[1]+3,'未见异常 ✔',style_other)
                            if val[1]==1:
                                sheet1.write(rowIndex11+41,val[1]+4,'炎症 ✔',style_other)
                            if val[1]==2:
                                sheet1.write(rowIndex11+41,val[1]+4,'结核:无  有 ✔ 活动  非活动',style_other)
                            if val[1]==3:
                                sheet1.write(rowIndex11+41,val[1]+3,'结核:无  有 ✔ 活动 ✔  非活动',style_other)
                            if val[1]==4:
                                sheet1.write(rowIndex11+41,val[1]+2,'结核:无  有 ✔ 活动  非活动 ✔',style_other)
                            if val[1]!=2 and val[1]!=3 and val[1]!=4:
                                sheet1.write(rowIndex11+41,6,'结核:无✔ 有  活动  非活动',style_other)
                            if val[1]==5:
                                sheet1.write(rowIndex11+41,val[1]+4,'肿瘤 ✔',style_other)
                        if isinstance(val,unicode):
                            sheet1.write(rowIndex11+41,11,val,style_other)
                    else:
                        sheet1.write(rowIndex11+41,11,val,style_other)

    table12Items=('SZSJ','SZBB')
    for key,value in dic['arg'][11].items():
        if key in table12Items:
            rowIndex12=table12Items.index(key)
            if len(value)!=0:
                for val in value:
                    if len(val)==2 and key=='SZSJ':
                        if isinstance(val,tuple):
                            sheet1.write(rowIndex12+42,val[1]+5,row_sz_one[val[1]]+'✔',style_other)
                        if isinstance(val,unicode):
                            if rowIndex12==0:sheet1.write(rowIndex12+42,10,val,style_other)
                    else:
                        if rowIndex12==0:sheet1.write(rowIndex12+42,10,val,style_other)
                        if rowIndex12==1:sheet1.write(rowIndex12+42,5,val,style_other)

    table13Items=('ZJHZYJ',)
    for key,value in dic['arg'][12].items():
        for val in value:
            if key=='ZJHZYJ':
                sheet1.write_merge(44,45,3,11,val,style_other)

    w.save(filename)

##tableDic1= {'FQZ': [(6, 1),(6,0)], 'SYZ_XPJJ': [(1, 2)], 'FSZ_GGO': [(0, 1)], 'ZQGKZ': [(3, 4)], 'FBZ': [(5, 6)], 'FJMS': [u'\u58eb\u5927\u592b\u4f3c\u7684'], 'FJZXWH': [(4, 5)], 'QG_ZQG': [(7, 1), (7, 3), u'\u540a\u6b7b\u6276\u4f24'], 'XWBH_JG': [(2, 3)]}
##tableDic2= {'XMZH': [(1, 1), (1, 3), (1, 5), (1, 7)], 'XMB': [(2, 1), u'\u53d1\u5c04\u70b9\u53d1\u751f'], 'XQJY': [(0, 2), (0, 4), (0, 6)]}
##tableDic3= {'XBZH': [(1, 3), u'\u7684\u9644\u5c5e\u516c\u53f8\u7684'], 'GZDMGH': [(0, 2)], 'XBJY': [], 'ZDMBB': [u'\u7b2c\u4e09\u65b9\u5e7f\u544a\u5546\u5730\u65b9'], 'FDMYC': [(5, 2), u'\u7b2c\u4e09\u65b9\u516c\u53f8'], 'XYZD': [(3, 5), u'\u5341\u591a\u4e2a']}
##tableDic4= {'LBJD': [(0, 1), u'\u8c46\u8150\u5e72d'], 'LBJGH': [(2, 1), u'\u5927\u8303\u7518\u8fea'], 'LBJX': [(1, 1), u'\u5730\u65b9']}
##tableDic5= {'ZGZW': [u'\u90fd\u7b26\u5408\u4e1c\u65b9'], 'SDBB': [(1, 3), (1, 4), u'\u7684\u53d1\u6325\u66f4\u5927'], 'JZXBB': [(2, 3), (2, 5), u'\u4e1c\u65b9\u5316\u5de5\u7684'], 'FJMS': []}
##tableDic6= {'XMRZZ': [], 'FJMS': [], 'LGYC': [(1, 2), (1, 3), u'\u70e6\u5f97\u5f88']}
##tableDic7= {'ZSTB': [(0, 0), u'\u83b7\u5f97\u4e30\u539a']}
##tableDic8= {'RXBB': [(0, 1), (0, 2), (0, 4), u'\u5c71\u4e1c\u5206\u516c\u53f8']}
##tableDic9= {'YXBB': [(3, 1), (3, 2), (3, 3), (3, 4), u'\u7684\u8bd7\u6b4c\u98ce\u683c\u58eb\u5927\u592b'], 'FQFM_HLBJ': [(4, 1), (4, 2), (4, 3), u'dfd '], 'GZBB': [(0, 3)], 'SZBB': [], 'SSXBB': [(1, 1), (1, 2), (1, 3), (1, 6), u'\u90fd\u662f\u975e\u5b98\u65b9\u7684']}
##tableDic10= {'QTBX': [u'\u662f\u6cd5\u5927\u5e08\u5085']}
##tableDic11= {'NIZHEN': [(0,0),(0, 1), (0, 5), u'\u5e45\u5ea6\u53d8\u5316\u5e45\u5ea6']}
##tableDic12= {'SZSJ': [(0, 1), (0, 3), u'\u5c81\u7684\u6cd5\u56fd'], 'SZBB': [u'\u6536\u8d39\u7684\u9ad8\u5bcc\u5e05\u7684\u6562\u6b7b\u961f\u98ce\u683c']}
##tableDic13= {'ZJHZYJ': [u'\u65e0\u75c5\u53d8\uff0c\u5065\u5eb7\u3002\n\t\t\t\t\t\t\t\t\t\t\t\t\t\u67d0\u67d0\u533b\u751f']}
##tableDic=tableDic1,tableDic2,tableDic3,tableDic4,tableDic5,tableDic6,tableDic7,tableDic8,tableDic9,tableDic10,tableDic11,tableDic12,tableDic13
##ExcelXlwt('Beijing_Excel03.xls',arg=tableDic)