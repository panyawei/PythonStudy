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
def Excellingcancer(filename):
    w=Workbook(encoding='utf-8')
    sheet1=w.add_sheet('first')

    alignment=Alignment()
    alignment.center=True
    style_top= XFStyle()
    fnt_top= Font()
    fnt_top
    fnt_top.name = u'微软雅黑'
    fnt_top.bold= True
    style_top.font= fnt_top

    style_other=XFStyle()
    fnt_other=Font()
    fnt_other.name=u'微软雅黑'
    style_other.font=fnt_other
    style_other.alignment=alignment

    sheet1.write_merge(0,1,0,11,'                    北京市肺癌基线调查及早期防治策略研究'
                        '低剂量螺旋CT结果记录表(肺结节)',style_top)
    sheet1.write_merge(2,2,0,11,'ID编号：                  姓名：                 性别：男 女                  年龄：                 检查日期：   年   月    日',style_top)
    column_left=[u'结节/肿块',u'结节/肿块位置(S肺段)',u'结节密度(实性=1、部分实性=2、非实性=3)',
                 u'结节距离最近胸膜的距离(mm)',u'长径(mm)',u'宽径(mm)',u'边缘光滑',u'边缘分叶',
                 u'毛刺及胸膜凹陷',u'是否牵拉胸膜',u'是否有液化',u'是否含钙化(量<1/2)',
                 u'结节出现序列',u'图像编号',u'建议复查时间',u'专家组会诊意见']
    i,j=0,3
    while i<len(column_left):
        sheet1.write_merge(j,j,0,1,column_left[i],style_top)
        j+=1
        i+=1
    row_one=[u'结节1',u'结节2',u'结节3',u'结节4',u'结节5',u'结节6',
             u'结节7',u'结节8',u'结节9',u'结节10']
    i,j=0,2
    while i<len(row_one):
        sheet1.write(3,j,row_one[i],style_other)
        j+=1
        i+=1
    column_other=[u'',u'',u'',u'',u'',u'Y      N',u'Y      N',u'Y      N',
                  u'Y      N',u'Y      N',u'Y      N',u'',u'',u'']
    i,j=0,4,
    for k in range(2,12):
        while i<len(column_other):
            sheet1.write(j,k,column_other[i],style_other)
            i+=1
            j+=1
        i,j=0,4
        k+=1
    sheet1.write_merge(18,18,2,8,'',style_other)
    sheet1.write_merge(18,18,9,11,'填表医师:',style_other)
    sheet1.write_merge(19,19,0,11,'注:1.结节内钙化大于病灶1/2的结节不需要填写;'
    '2.结节部位填写:右侧-R,左侧-L表示,后面填写肺段S(1-10),如右上叶尖端为RS1。',style_other)
    w.save(filename)
if __name__=='__main__':
    Excellingcancer('Beijing_lungcaner.xls')


