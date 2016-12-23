# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     21/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lm = {'name':'liming','age':'25','language':'80','math':'75','english':'85'}
    zq = {'name':'zhangqiang','age':'23','language':'75','math':'82','english':'78'}
    lm['python']='60'
    zq['python']='80'
    print lm
    print zq

    zq['math']='89'
    print zq

    del lm['age']
    print lm

    dic = {1:{'name':'liming','age':'25','language':'80','math':'75','english':'85'},
            2:{'name':'zhangqiang','age':'23','language':'75','math':'82','english':'78'}}
    dic[1]['python']='60'
    dic[2]['python']='80'

    dic[3]={'name':'zhangqiang','age':'23','language':'75','math':'82','english':'78'}

    print dic
    print dic[1]
    print dic[2]
    dic[2]['math']='89'
    print dic[2]
    del dic[1]['age']
    print dic[1]

    for key,value in dic.items():
        print key,'==>',value
    for key in dic.iteritems():
        print key
main()
##if __name__ == '__main__':
##    main()
