#coding=utf-8
# mysetup.py
from distutils.core import setup
import py2exe
import sys
import os

def list(path, dirlist = [], suffix = ""):
	fileobj = os.listdir(path)
	for f in fileobj:
		if (os.path.isfile(path + '/' + f) & (f[-3:] == suffix) & (f <> "mysetup.py")):
			dirlist.append(f)
			pass
		pass
	pass

includes = ["encodings", "encodings.*"]
sys.argv.append("py2exe")
options = {"py2exe": {"bundle_files": 1}}
path = os.getcwd()
dirlist = []
print(path[len(path) - 1] != '\\')
if path[len(path) - 1] != '\\':
	path += '\\'
	pass
print(path)

if __name__ == '__main__':
	list(path, dirlist, ".py")
	print(dirlist)
	szStbuf = raw_input("请输入要转换的python文件名:")
	setup(options=options, zipfile=None, console=[{"script": szStbuf}])
