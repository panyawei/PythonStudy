# -*- coding:utf-8 -*-

import pypinyin
##row_chest_one=[u'左侧',u'右侧',u'双侧',u'少量',u'中量',u'大量']
##fb_row_chest_one=[]
##for name in row_chest_one:
##    py_row_chest_one=pypinyin.slug((name))
##    sx_row_chest_one=list(py_row_chest_one.split('-')[0])[0]+list(py_row_chest_one.split('-')[1])[0]
##    fb_row_chest_one.append(sx_row_chest_one.upper())
##print fb_row_chest_one

column_chest=[u'胸膜积液',u'胸膜增厚',u'胸膜斑']
print column_chest
fb_column_chest=[]
for name in column_chest:
    print name,len(name)
    py_column_chest=pypinyin.slug(name)
    print py_column_chest

    if len(name)==4:
        sx_column_chest=list(py_column_chest.split('-')[0])[0]+list(py_column_chest.split('-')[1])[0]+list(py_column_chest.split('-')[2])[0]+list(py_column_chest.split('-')[3])[0]
        fb_column_chest.append(sx_column_chest.upper())
    if len(name)==3:
        sx_column_chest=list(py_column_chest.split('-')[0])[0]+list(py_column_chest.split('-')[1])[0]+list(py_column_chest.split('-')[2])[0]
        fb_column_chest.append(sx_column_chest.upper())
print fb_column_chest
