# -*- coding:utf-8 -*-
from urllib import urlencode
from urllib2 import Request,urlopen,build_opener,HTTPCookieProcessor,install_opener
url="http://bbs.chinaunix.net/member.php?mod=logging@action=login@loginsubmit" \
    "=yes@loginhash=L768q"
postdata=urlencode({
    "username":"虚拟的背后",
    "password":"weiqing203010"
}).encode('utf-8')  # 编码
req=Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")

data=urlopen(req).read()
handle=open("G://e1.html","wb")
handle.write(data)
handle.close()

url2="http://bbs.chunaunix.net/"
req2=Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")
data2=urlopen(req2).read()
handle2=open('G://e2.html',"wb")
handle2.write(data2)
handle2.close()
