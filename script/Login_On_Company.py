# -*- coding: cp936 -*-
import urllib
import urllib2
import os
import time
# 登录的主页面
hosturl = 'http://10.16.99.15/webAuth/'  # 自己填写
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
# 从数据包中分析出，处理post请求的url
posturl = "http://10.16.99.15/webAuth/"

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
# cj = cookielib.LWPCookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)

# 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
# h = urllib2.urlopen(hosturl)

# 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Referer': 'http://10.16.99.15/webAuth/',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
# 构造Post数据，他也是从抓大的包里分析得出的。
postData = {
    'username': "xuwb",
    'password': "wlwzzfz654.",
    'pwd': "wlwzzfz654.",
    "secret": 'true'
}

# 需要给Post数据编码
postData = urllib.urlencode(postData)

# 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
response = urllib2.urlopen(request)
text1 = response.read()
print text1.decode("UTF8")
time.sleep(3)