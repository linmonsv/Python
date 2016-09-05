__author__ = 'xwb'
#coding=utf-8
import sys
import os
from ctypes import *

def list(path, dirlist= [],suffix = ""):
	fileobj = os.listdir(path)
	for f in fileobj:
		if (os.path.isfile(path + '/' + f) & (f[0-len(suffix):] == suffix)):
			dirlist.append(f)
			pass
		pass
	pass


def getpwd():
	path = os.getcwd()
	if path[len(path) - 1] != '\\':
		path += '\\'
		pass
	return path
	pass



if __name__ == '__main__':

	path = ""
	dirlist = []
	path = getpwd()
	list(path, dirlist, ".dll")
	print dirlist

	dll = windll.LoadLibrary("MisPos.dll")

	inputData = raw_input(u"请输入入参字符串:".encode("GBK"));

	strRequest = create_string_buffer(inputData, 221)
	strResponse = create_string_buffer(1024)
	strFuncName = "bankall"

	pRequest = c_char_p()
	pResponse = c_char_p()

	pRequest.value = addressof(strRequest)
	pResponse.value = addressof(strResponse)
	strExec = "dll." + strFuncName + '(strRequest, addressof(strResponse))'
	print(strExec)
	print(eval(strExec))
	#print(codecs.decode(b"\xc3\xdc\xc2\xeb\xbc\xfc\xc5\xcc\xc1\xac\xbd\xd3\xca\xa7\xb0\xdc\xa3\xac\xc7\xeb\xbc\xec\xb2\xe9", 'UTF-8'))
	print(pResponse.value.decode("GBK"))
	inputData = raw_input(u"输入其他按键退出此程序".encode("GBK"));