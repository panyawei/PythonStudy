# -*- coding:utf-8 -*-
# 全局匹配函数  compile
import re
string="asdbpythondfpythonsdfgpython"
pattern=re.compile('.python') # 预编译
result=pattern.findall(string)
print result
if result:
    print result[0:2]