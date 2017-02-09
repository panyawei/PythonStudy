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

import xlsxwriter

# 建文件及sheet.
workbook = xlsxwriter.Workbook('z.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells. 设置粗体，默认是False
bold = workbook.add_format({'bold': True})

# Add a number format for cells with money.  定义数字格式
money = workbook.add_format({'num_format': '$#,##0'})

# Write some data headers. 带自定义粗体blod格式写表头
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# Some data we want to write to the worksheet.
expenses = (
 ['Rent', 1000],
 ['Gas',   100],
 ['Food',  300],
 ['Gym',    50],
)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
 print item,cost
 worksheet.write(row, col,     item)    # 带默认格式写入
 worksheet.write(row, col + 1, cost, money)  # 带自定义money格式写入
 row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total',       bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)


workbook.close()