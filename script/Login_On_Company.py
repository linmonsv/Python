# -*- coding: cp936 -*-
import urllib
import urllib2
import os
import time
# ��¼����ҳ��
hosturl = 'http://10.16.99.15/webAuth/'  # �Լ���д
# post���ݽ��պʹ����ҳ�棨����Ҫ�����ҳ�淢�����ǹ����Post���ݣ�
# �����ݰ��з�����������post�����url
posturl = "http://10.16.99.15/webAuth/"

# ����һ��cookie��������������ӷ���������cookie�����أ������ڷ�������ʱ���ϱ��ص�cookie
# cj = cookielib.LWPCookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)

# �򿪵�¼��ҳ�棨����Ŀ���Ǵ�ҳ������cookie����������������post����ʱ����cookie�ˣ������Ͳ��ɹ���
# h = urllib2.urlopen(hosturl)

# ����header��һ��header����Ҫ����һ������������Ǵ�ץ���İ�������ó��ġ�
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Referer': 'http://10.16.99.15/webAuth/',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
# ����Post���ݣ���Ҳ�Ǵ�ץ��İ�������ó��ġ�
postData = {
    'username': "xuwb",
    'password': "wlwzzfz654.",
    'pwd': "wlwzzfz654.",
    "secret": 'true'
}

# ��Ҫ��Post���ݱ���
postData = urllib.urlencode(postData)

# ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼����
request = urllib2.Request(posturl, postData, headers)
response = urllib2.urlopen(request)
text1 = response.read()
print text1.decode("UTF8")
time.sleep(3)