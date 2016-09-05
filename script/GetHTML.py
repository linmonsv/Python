#coding=utf-8
import urllib
import re
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read();
	return html
	pass
html = getHtml("http:\\")  

print (html)
