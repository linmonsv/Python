#coding=utf-8
import random
#import pdb
def Nim(obj):
	print obj
	i = 0
	num = 0
	if obj[0] + obj[1] + obj[2] == 1:
		num = 1
		if obj[0] == 1:
			i = 1
			pass
		elif obj[1] == 1:
			i = 2
			pass
		elif obj[2] == 1:
			i = 3
			pass
		pass
	elif obj[0] >= obj[1] and obj[0] >= obj[2]:
		num = obj[0] - (obj[1] ^ obj[2])#������������
		if num > obj[0]:
			num = random.randint(1, obj[0])
			pass
		i = 1
	elif obj[1] >= obj[0] and obj[1] >= obj[2]:
		num = obj[1] - (obj[0] ^ obj[2])#������������
		if num > obj[1]:
			num = random.randint(1, obj[1])
			pass
		i = 2
	elif obj[2] >= obj[0] and obj[2] >= obj[1]:
		num = obj[2] - (obj[0] ^ obj[1])#������������
		if num > obj[2]:
			num = random.randint(1, obj[2])
			pass
		i = 3
	obj[i - 1] -= num
	print ("���������˵�%d��%d������" %(i,num));
	print obj
	return obj

def main():
	obj = []
	for i in range(3):
		obj.append(random.randint(1, 10))
	print obj
	while (obj[0] + obj[1] + obj[2] != 0):
		i = 0
		num = 0
		i = eval(raw_input("��������Ҫ������һ�ѵ�����"));
		while i <= 0 or i > 3 or obj[i - 1] <= 0:
			print("���������������\n");
			i = eval(raw_input("��������Ҫ������һ�ѵ�����"));

		num = eval(raw_input("��������Ҫ���߶�������"));
		while num <= 0 or num > obj[i - 1]:
			print("���������������\n");
			num = eval(raw_input("��������Ҫ���߶�������"));	

		obj[i - 1] -= num
		if obj[0] + obj[1] + obj[2] == 0:
			break
		obj = Nim(obj)
		pass
	pass     

if __name__ == '__main__':
	main()
