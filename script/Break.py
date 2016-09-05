# -*- coding: UTF-8 -*-
__author__ = 'xwb'
import win32clipboard
import win32con

def Break():
	Ret = "";
	win32clipboard.OpenClipboard()
	cFormat = win32clipboard.GetClipboardData(win32con.CF_TEXT)
	Ret = raw_input("确认输入的字符串为\n" + cFormat)
	if ( Ret == 'n' or Ret == 'N' ):
		cFormat = raw_input("请输入字符串")
		cFormat = repr(cFormat)
		pass
	cResult = ""
	for i in range(0, len(cFormat), 2):
		cResult += cFormat[i:i + 2]
		cResult += " "
		pass
	print(cResult)
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(cResult)
	win32clipboard.CloseClipboard()
	pass

if __name__ == '__main__':
	Break()