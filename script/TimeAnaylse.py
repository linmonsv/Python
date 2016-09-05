# coding=utf8
import win32clipboard
import win32con

fp = open ( u"时间消耗.txt", "r" )
szContext = ""
lClass = []
lTemp = []
while True:
	szContext = fp.readline ( )
	szTemp = szContext.decode ( "utf8" )
	if len(szContext) < 5 :
		break;
	if szTemp.find("tv_usec:[") == -1:
		pass
	else:
		lTemp.append ( szTemp[szTemp.find ( "tv_usec:[" ) + 9 : szTemp.rfind("]")] )
		pass
	pass
for i in range ( len ( lTemp ) ):
	Total = int(lTemp[i]) - int(lTemp[0]);
	Next = int(lTemp[i]) - int(lTemp[i - 1]);
	print("Total+" + str(Total )+ " "),
	print("Next+" + str (Next))
fp.close()