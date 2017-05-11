# -*- coding:utf-8 -*-
import urlparse
from urllib import urlencode,urlopen
from urllib2 import Request
url="http://bbs.chinaunix.net/member.php?mod=logging@action=login@loginsubmit" \
    "=yes@loginhash=L768q"
postdata=urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')  # 编码
req=Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
     51.0.2704.79 Safari/537.36 Edge/14.14393")
data=urlopen(req).read()
handle=open("G://e1.html","wb")
handle.write(data)
handle.close()