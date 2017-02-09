# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     09/02/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlrd
import xlwt
import datetime
##def testXlrd(filename):
##    book=xlrd.open_workbook(filename)
##    sh=book.sheet_by_index(0)
##    print "Worksheet name(s): ",book.sheet_names()[0]
##    print 'book.nsheets',book.nsheets
##    print 'sh.name:',sh.name,'sh.nrows:',sh.nrows,'sh.ncols:',sh.ncols
##    print 'A1:',sh.cell_value(rowx=0,colx=1)
##    #如果A3的内容为中文
##    print 'A2:',sh.cell_value(0,2).encode('gb2312')
def testXlwt(filename):
    book=xlwt.Workbook()
    sheet1=book.add_sheet('hello')
    book.add_sheet('word')
    sheet1.write(0,0,'hello')
    sheet1.write(0,1,'world')
    sheet1.write_merge(2,2,1,3,'ok') #合并单元格

    row1 = sheet1.row(1)
    row1.write(0,'A2')
    row1.write(1,'B2')
    sheet1.col(0).width = 10000
    sheet2 = book.get_sheet(1)
    sheet2.row(0).write(0,'Sheet 2 A1')
    sheet2.row(0).write(1,'Sheet 2 B1')
    sheet2.flush_row_data()
    sheet2.write(1,0,'Sheet 2 A3')
    sheet2.col(0).width = 5000
    sheet2.col(0).hidden = True
##    sheet2.write_merge(3,3,0,3,'ok')
    book.save(filename)
if __name__=='__main__':
##    testXlrd(u'helloWorld.xls')
    testXlwt('helloWorld.xls')
    base=datetime.date(1899,12,31).toordinal()
    tmp=datetime.date(2013,07,16).toordinal()
    print datetime.date.fromordinal(tmp+base-1).weekday()