# -*- coding:utf-8 -*-
import urllib2
from urllib2 import request_host
import re,sys
import os,glob
import xlwt
import codecs
import chardet
book=xlwt.Workbook()
sheet=book.add_sheet('sheet',cell_overwrite_ok=True)
resultA=[]
resultB=[]
resultC=[]
resultD=[]
resultE=[]
for i in range(0,2):
    content=urllib2.urlopen("http://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="+str(i)).read()
##    print 'html=',html
    typeEncode=sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding','utf-8')
    html = content.decode(infoencode,'ignore').encode(typeEncode)
    pat1=u'onmousedown=""(.+?)'
    pat2=u'<span class="t2"(.*?)</span>>'
##    resulta=re.findall(re.compile(pat1),str(html))
    resulta=re.compile(pat1).findall(str(html))
    resultA.extend(resulta)
    print resultA
##    resultB.extend(resultb)
    sheet.write(0,0,'zwyx')
    sheet.write(0,1,'gzdd')
    for k in range(0,len(resultA)):

        try:
##            print 'ssss'
            zw=resultA[k]
##            gz=resultB[k]
            sheet.write(k+1,0,zw)
##            sheet.write(k+1,1,gz)

        except Exception as e:
            print e
            continue
    book.save('d:\\zlzp.xls')