import os
import win32clipboard
import win32con

win32clipboard.OpenClipboard()
szBuf = win32clipboard.GetClipboardData(win32con.CF_TEXT)
win32clipboard.CloseClipboard()

os.system("explorer " + szBuf)