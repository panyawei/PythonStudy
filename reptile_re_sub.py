# -*- coding:utf-8 -*-
# re.sub()实现替换某些字符串
# re.sub(pattern,rep,string,max)  max可选参数
import re
string="hellomypyhtonddfgpythonfdsgspythonddfgpythona"
pattern="python."
result=re.sub(pattern,"php",string)
result1=re.sub(pattern,"php",string,2)
print result
print result1