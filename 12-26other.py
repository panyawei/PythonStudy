# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     26/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# repr函数和反引号用来获取对象的可打印的表示形式
i = []
i.append('ok')
print `i`
print repr(i)

# assert语句用来声明某个条件是真的,当assert语句失败的时候，会引发一个AssertionError
mylist = ['item']
assert len(mylist)>=1
print mylist.pop()

# assert len(mylist)>=5 ==> 一个AssertionError

# exec语句用来执行储存在字符串或文件中的Python语句
exec 'print "Hello World"'

#eval语句用来计算存储在字符串中的有效Python表达式
print eval('2*5')
