#coding=utf-8
import win32clipboard as a
import win32con

raw_input("��ȷ�ϸ��Ƹ�ʽ�ַ��������а���")
a.OpenClipboard()
cFormat = a.GetClipboardData(win32con.CF_TEXT)
cFormat = cFormat.strip('\x00').strip().replace('\n', '').replace('\t', '').replace('\r', '')
print (repr(cFormat))
a.EmptyClipboard()
a.CloseClipboard()

raw_input("��ȷ�ϸ��ƶ�Ӧ�ı������鵽���а���")
a.OpenClipboard()
cStr = a.GetClipboardData(win32con.CF_TEXT)
cStr = cStr.strip('\x00').strip().replace('\n', '').replace('\t', '').replace('\r', '')
print (repr(cStr))
a.EmptyClipboard()
a.CloseClipboard()

caStr =  cStr.split(',')
caFormat = cFormat.split('%')

i = 0
j = 0
while i < len(caFormat):
	if caFormat[i] == "":
		i = i + 1
		pass
	else:
		print ("%" + caFormat[i] + "------->>" + caStr[j])
		j = j + 1
		i = i + 1
		pass
	pass
raw_input("�����ʾ����")