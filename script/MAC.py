# coding=cp936
from Crypto.Cipher import DES
import os
import binascii
def MACCalc(list=[], mackey=""):
	stroutput = list[0]
	for i in range(1, len(list), 1):
		str1 = bin(int(stroutput, 16))
		str2 = bin(int(list[i], 16))
		strinput = str1 + ' ^ ' + str2
		print (strinput)
		print ("\n")
		stroutput = eval(strinput)
		stroutput = str(hex(stroutput)[2:-1]).upper()
		pass
	pass
	print (stroutput)
	stroutput = binascii.b2a_hex(stroutput)

	# cipher = DES.new(binascii.a2b_hex(mackey), 1, '')
	# msg = cipher.encrypt(binascii.a2b_hex(stroutput[0:16]))
	# msg = binascii.b2a_hex(msg).upper()
	# print (msg)
	# str1 = bin(int(msg, 16))
	# str2 = bin(int(stroutput[16:32], 16))
	# strinput = str1 + ' ^ ' + str2
	# stroutput = eval(strinput)
	# stroutput = str(hex(stroutput)[2:-1]).upper().rjust(16, '0')

	# msg = cipher.encrypt(binascii.a2b_hex(stroutput.replace(' ', '')))
	# msg = binascii.b2a_hex(binascii.b2a_hex(msg).upper())
	# print (msg[0:16])

if __name__ == '__main__':
	strMsg = raw_input("\n")
	#strMsg = "02 00 32 00 00 00 00 C0 80 01 00 00 00 00 00 00 00 00 01 00 18 33 31 31 38 39 37 38 31 36 33 32 34 38 38 38 32 35 35 30 30 30 30 30 31 39 30 32 30 31 35 31 30 31 30 30 30 30 30 32 39 33 31 35 36"
	# strMsg = "02 00 3C 00 00 00 00 C0 80 01 21 00 00 00 00 00 00 00 01 22 30 30 30 30 30 32 35 38 32 30 31 36 30 32 31 35 31 31 35 37 34 38 07 38 2E 38 2E 38 2E 38 30 30 30 30 30 32 35 38 32 30 31 35 31 31 31 38 30 30 30 30 33 30 30 31 35 36 "
	strMsg = strMsg.replace(' ', '')
	strKey = "49B3E9FE7CBABCC4"
	#strKey = raw_input("\n")
	strKey = strKey.replace(' ', '')
	print (strMsg)
	listMsg = []
	i = 0
	for i in range(32, len(strMsg)-1, 32):
		if i <= len(strMsg):
			listMsg.append(strMsg[i-32 : i])
			pass
		pass
	i = i + 32
	listMsg.append(strMsg[i-32 : len(strMsg)].ljust(32, '0'))
	print (listMsg)
	MACCalc(listMsg, strKey)
	# MACCalc(listMsg, "E83FDC9464EE571C");