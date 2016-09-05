# coding=utf8
import win32clipboard
import win32con

win32clipboard.OpenClipboard()
szStbuf = win32clipboard.GetClipboardData(win32con.CF_TEXT)
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()
# szStbuf = raw_input(":")
fp = open ( "Stru.txt", "r" )
szContext = ""
lClass = []
lTemp = []
while True:
	szContext = fp.readline ( )
	szTemp = szContext.decode ( "utf8" )
	if szContext and len ( szContext ) > 5:
		# print(szContext.decode("GBK")),
		if szContext.decode ( "utf8" ).find ( "char" ) == True:

			szTemp = szTemp.replace ( "char", "" ).replace ( " ", "" ).strip ( )
			lTemp = []
			if szTemp.find("[") == -1:
				lTemp.append ( szTemp[:szTemp.find ( ";" )] )
				lTemp.append ("1")
				lTemp.append ( szTemp[szTemp.find ( "/" ):len ( szTemp )] )
				pass
			else:
				lTemp.append ( szTemp[:szTemp.find ( "[" )] )
				lTemp.append ( szTemp[szTemp.find ( "[" ) + 1:szTemp.find ( "]" )] )
				lTemp.append ( szTemp[szTemp.find ( "/" ):len ( szTemp )] )
				pass
			lTemp.append("")
			lClass.append ( lTemp )
	elif szContext and 5 >= len ( szContext ):
		continue
	else:
		break
	pass
lengh = 0
for i in range ( len ( lClass ) ):
	print(lClass[i][0]),
	print(lClass[i][1]),
	print(lClass[i][2])
	lengh = lengh + int(lClass[i][1])
	print(lengh)
fp.close()
j = 0
for k in range( len(lClass) ):
	lClass[k][3] += szStbuf[j : int(lClass[k][1]) + j]
	j += int(lClass[k][1])
	pass
fp = open(u"分析结果.txt", 'w')

for i in range ( len ( lClass ) ):
	#print(lClass[i][3]),
	#print(lClass[i][2])
	fp.write("[" + lClass[i][3] +"]     " +lClass[i][2].encode("GBK") + '\n')

for i in range ( len ( lClass ) ):
	fp.write("memcpy( ." + lClass[i][0].encode("GBK") +", , " +lClass[i][1].encode("GBK") + ");" +lClass[i][2].encode("GBK")+ '\n')
