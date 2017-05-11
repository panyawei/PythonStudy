# -*- coding:utf-8 -*-
# 在pyscript中可以顺利运行

from urllib import urlencode
from urllib2 import Request,urlopen,build_opener,HTTPCookieProcessor,install_opener
import cookielib
url="http://bbs.chinaunix.net/member.php?mod=logging@action=login@loginsubmit" \
    "=yes@loginhash=L768q"
postdata=urlencode({
    "username":"虚拟的背后",
    "password":"weiqing203010"
}).encode('utf-8')  # 编码
req=Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")
# 获取Cookiejar对象（存在本机的cookie消息）
clib=cookielib.CookieJar()

# 创建cookie处理器，并构建opener对象
opener=build_opener(HTTPCookieProcessor(clib))
# 将opener设置为全局
install_opener(opener)
file=opener.open(req)
data=file.read()
file=open('G://f1.html','wb')
file.write(data)
file.close()


url2="http://bbs.chunaunix.net/"
data2=urlopen(url2).read()
handle2=open('G://f2.html',"wb")
handle2.write(data2)
handle2.close()
