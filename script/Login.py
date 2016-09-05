#!/usr/bin/python
# coding=UTF-8

import urllib
import urllib2
import cookielib
import ConfigParser
import os
# 输入用户名和密码

cf = ConfigParser.ConfigParser()
bRet = os.path.exists('Config.ini')
if bRet is False:
    fp = open("Config.ini", "w")
    cf.add_section("baseconf")
    cf.write(fp)
    fp.close()
    fp = open("Config.ini", "w")
    cf.set("baseconf", "user", "test")
    cf.set("baseconf", "password", "test")
    cf.write(fp)
    fp.close()
    pass

cf.read("Config.ini")
db_user = cf.get("baseconf", "user")
db_pwd = cf.get("baseconf", "password")
print "用户名为" + db_user
print "密码为" + db_pwd
str_confirm = raw_input("请确认是否是此用户和密码,默认为Yes(y for Yes And n for No):")
if str_confirm == "N" or str_confirm == "No" or str_confirm == "no" or str_confirm == "n":
    db_user = raw_input("请输入用户名:")
    db_pwd = raw_input("请输入密码:")
    cf.set("baseconf", "user", db_user)
    cf.set("baseconf", "password", db_pwd)
    cf.write(open("Config.ini", "w"))

# 登录的主页面
hosturl = 'http://passport.vpgame.com/'  # 自己填写
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
# 从数据包中分析出，处理post请求的url
posturl = "http://passport.vpgame.com/login.html?redirect=http://www.vpgame.com/"

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

# 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

# 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Referer': 'http://passport.vpgame.com/login.html?redirect=http://www.vpgame.com/'
}
# 构造Post数据，他也是从抓大的包里分析得出的。
postData = {
    'Register[username]': db_user,
    'Register[password]': db_pwd,
    'Register[rememberMe]': 0,
}

# 需要给Post数据编码
postData = urllib.urlencode(postData)
# 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
response = urllib2.urlopen(request)
text1 = response.read()
response = urllib2.urlopen("http://www.vpgame.com/user/default/checkin.html")
text1 = response.read()
fp = open('checkin.html', 'w')
fp.write(text1)
fp.close()
raw_input("请打开同级目录下的checkin.html 查看是否已经签到完毕 回车以退出此程序")