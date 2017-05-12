# -*- coding:utf-8 -*-
import re,os,time
from urllib2 import Request,urlopen,URLError
from urllib import urlretrieve
def craw(url,page):
    html1=urlopen(url).read()
    html1=str(html1)
    # print 'html1=',html1
    pattern1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pattern1).findall(html1)
    if len(result1)<1:
        result1=html1.split('<div id="plist"')[1]
        result1=result1.split('<div class="page clearfix">')[0]
    else:
        print 'result1=',result1
        result1=result1[0]
    # print 'result1=',result1
    pattern2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist=re.compile(pattern2).findall(result1)
    print 'imagelist=',imagelist
    x=1
    for imageurl in imagelist:
        files='F:/reptile'
        if os.path.isdir(files):
            imagename='F:/reptile/%s.jpg' % (time.time())
            imageurl="http://"+imageurl
            try:
                urlretrieve(imageurl,imagename)
            except URLError as e:
                if hasattr(e,"code"):
                    x+=1
                if hasattr(e,"reason"):
                    x+=1
        x+=1
for i in range(1,2):
    url="https://list.jd.com/list.html?cat=670,671,672&page="+str(i)
    craw(url,i)