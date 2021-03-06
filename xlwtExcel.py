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
import xlwt #exampleB
from xlwt import *
##class xlwtExcel:
def ExcelXlwt(filename,**args):


    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet('first',cell_overwrite_ok = True)
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
    sheet1.write(4,10,'中',style_other)
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
    sheet1.write_merge(12,12,3,11,'        附加描述:',style_other_other)
    sheet1.write_merge(13,13,3,4,'气管/支气管',style_other)
    sheet1.write(13,6,'结节',style_other)
    sheet1.write_merge(13,13,7,8,'管壁增厚',style_other)
    sheet1.write(13,9,'腔狭窄',style_other)
    sheet1.write_merge(13,13,10,11,'部位:',style_other)

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
    sheet1.write_merge(16,16,6,11,'胸膜病变补充:',style_other_other)

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
    sheet1.write_merge(18,18,8,11,'其它:',style_other_other)
    row_bloodvessel_three=['局限','弥漫']
    i,j=0,19
    while i<len(row_bloodvessel_three):
        sheet1.write(j,i+6,row_bloodvessel_three[i],style_other)
        i+=1
    sheet1.write_merge(19,19,8,11,'少量           中量          大量',style_other)
    row_bloodvessel_four=['左心室','右心室','左心房','右心房','普大','其它']
    i,j=0,20
    while i<len(row_bloodvessel_four):
        sheet1.write(j,i+6,row_bloodvessel_four[i],style_other)
        i+=1
    row_bloodvessel_five=['壁钙化','动脉瘤']
    i,j=0,21
    while i<len(row_bloodvessel_five):
        sheet1.write(j,i+6,row_bloodvessel_five[i],style_other)
        i+=1
    sheet1.write_merge(21,21,8,11,'其它:',style_other_other)
    row_bloodvessel_six=['左PA','右PA']
    i,j=0,22
    while i<len(row_bloodvessel_six):
        sheet1.write(j,i+6,row_bloodvessel_six[i],style_other)
        i+=1
    sheet1.write_merge(22,22,8,11,'描述:',style_other_other)

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
        sheet1.write_merge(j,j,6,11,'部位:',style_other_other)


    # mediastinumLesion
    sheet1.write_merge(26,29,0,2,'纵隔病变',style_top)
    column_zgbb=['纵隔占位','食道病变','甲状腺病变']
    i,j=0,26
    while i<len(column_zgbb):
        sheet1.write_merge(j,j,3,4,column_zgbb[i],style_other)
        i+=1
        j+=1
    sheet1.write_merge(29,29,3,11,'        附加描述:',style_other_other)
    for j in range(26,30):
        sheet1.write(j,5,'无/有',style_other)

    sheet1.write_merge(26,26,6,11,'部位及描述:',style_other_other)
    sheet1.write(27,6,'上段',style_other)
    sheet1.write(27,7,'中段',style_other)
    sheet1.write(27,8,'下端',style_other)
    sheet1.write_merge(27,27,9,11,'补充:',style_other_other)
    row_zgbb_three=['左叶','右叶','弥漫','实性','蘘性','其它:']
    i,j=0,28
    while i<len(row_zgbb_three):
        sheet1.write(j,i+6,row_zgbb_three[i],style_other)
        i+=1

    # Chest wall lesion
    sheet1.write_merge(30,32,0,2,'胸壁病变',style_top)
    sheet1.write_merge(30,30,3,4,'胸壁软组织',style_other)
    sheet1.write_merge(31,31,3,4,'肋骨异常',style_other)
    sheet1.write_merge(32,32,3,11,'        附加描述:',style_other_other)
    for j in range(30,32):
        sheet1.write(j,5,'无/有',style_other)
    row_xbbb=['右侧','左侧']
    i,j=0,30
    for j in range(30,32):
        while i<len(row_xbbb):
            sheet1.write(j,i+6,row_xbbb[i],style_other)
            i+=1
        sheet1.write_merge(j,j,8,11,'描述:',style_other_other)
        i=0

    # Vertebral anomalies
    sheet1.write_merge(33,33,0,2,'椎体异常',style_top)
    sheet1.write_merge(33,33,3,4,'增生退变',style_other)
    sheet1.write_merge(33,33,5,11,'    其它:',style_other_other)

    # Breast lesions
    sheet1.write_merge(34,34,0,2,'乳腺病变',style_top)
    row_rxbb=['右侧','左侧','钙化','结节','占位']
    i,j=0,34
    for j in range(34,35):
        sheet1.write_merge(34,34,3,4,'',style_other)
        sheet1.write_merge(34,34,10,11,'描述:',style_other_other)
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
    sheet1.write_merge(j,j,6,9,'    蘘肿:    无    有    单发   多发',style_other_other)
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
    sheet1.write_merge(j,j,9,11,'描述:',style_other_other)
    while i<len(row_sfb_four):
        sheet1.write(j,i+6,row_sfb_four[i],style_other)
        i+=1
    row_sfb_five=['肿大','钙化']
    i,j=0,39
    sheet1.write_merge(j,j,8,11,'    其它:',style_other_other)
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
    sheet1.write_merge(41,41,9,11,'其它:',style_other_other)

    # follow-up
    sheet1.write_merge(42,43,0,2,'随诊建议',style_top)
    sheet1.write_merge(42,42,3,4,'随诊时间',style_other)
    sheet1.write_merge(43,43,3,4,'随诊表现',style_other)
    row_sz_one=['一个月','三个月','六个月','十二个月']
    i,j=0,42
    while i<len(row_sz_one):
        sheet1.write(j,i+5,row_sz_one[i],style_other)
        i+=1
    sheet1.write_merge(42,42,9,11,'其它建议:',style_other_other)
    row_sz_two=['','','','','','','']
    i,j=0,43
    while i<len(row_sz_two):
        sheet1.write(j,i+5,row_sz_two[i],style_other)
        i+=1

    chestDic=args
    print 'chestDic=',chestDic
    for key,value in chestDic['arg1'].items():
##        column_chest=['胸膜积液','胸膜增厚','胸膜斑']

        if key=='XQJY':
            for val in value:
                import pypinyin
                fb_row_chest_one=[]
                for name in row_chest_one:
                    py_row_chest_one=pypinyin.slug(name)
                    sx_row_chest_one=list(py_row_chest_one.split('-')[0])[0]+list(py_row_chest_one.split('-')[1])[0]
                    fb_row_chest_one.append(sx_row_chest_one.upper())
##                print fb_row_chest_one
                if val in fb_row_chest_one:
                    sheet1.write(14,5,'有   ✔',style_other)
##                    print '111'

                    index=fb_row_chest_one.index(val)
                    pop=row_chest_one.pop(index)
                    row_chest_one.insert(index,pop+u'    ✔')
                    print 'row_chest_one=',row_chest_one
                    i,j=0,14
                    while i<len(row_chest_one):
                        sheet1.write(j,i+6,row_chest_one[i],style_other)
                        i+=1
                else:
                    sheet1.write(14,5,'无   ✔',style_other)
        elif key=='XMZH':
            for val in value:
                import pypinyin
                fb_row_chest_two=[]
                for name in row_chest_two:
                    py_row_chest_two=pypinyin.slug(name)
                    sx_row_chest_two=list(py_row_chest_two.split('-')[0])[0]+list(py_row_chest_two.split('-')[1])[0]
                    fb_row_chest_two.append(sx_row_chest_two.upper())
                if val in fb_row_chest_two:
                    sheet1.write(15,5,'有   ✔',style_other)
##                    print '222'
                    index=fb_row_chest_two.index(val)
                    pop=row_chest_two.pop(index)
                    row_chest_two.insert(index,pop+u'    ✔')
                    i,j=0,15
                    while i<len(row_chest_two):
                        sheet1.write(j,i+6,row_chest_two[i],style_other)
                        i+=1
                else:
                    sheet1.write(15,5,'无   ✔',style_other)

    w.save('E:\github\PythonStudy\\'+filename)

chestDic={'XQJY':['DL','ZC'],'XMZH':['GF','YC','GH']}
ExcelXlwt('Beijing_Excel03.xls',arg1=chestDic)