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

	strRequest = create_string_buffer(b"D2015   A001    5300000000000120121119000000000167000000000098000000000002720305000000000015                                     33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333                                   W20150616205755001                                                                                                                                                                                                                                                                                                              ", 588)
	# strRequest2 = create_string_buffer(b"9999", 4)
	strResponse = create_string_buffer(1024)
	strFuncName = "BankTrans"

	pRequest = c_char_p()
	pResponse = c_char_p()

	pRequest.value = addressof(strRequest)
	pResponse.value = addressof(strResponse)
	strExec = "dll." + strFuncName + '(strRequest, addressof(strResponse))'
	print(strExec)
	print(eval(strExec))
	#print(codecs.decode(b"\xc3\xdc\xc2\xeb\xbc\xfc\xc5\xcc\xc1\xac\xbd\xd3\xca\xa7\xb0\xdc\xa3\xac\xc7\xeb\xbc\xec\xb2\xe9", 'UTF-8'))
	print(pResponse.value.decode("GBK"))