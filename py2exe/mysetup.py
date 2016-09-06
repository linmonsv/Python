#coding=utf-8
# mysetup.py
from distutils.core import setup
import py2exe
import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore

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
	# list(path, dirlist, ".py")
	# print(dirlist)
	# szStbuf = raw_input("请输入要转换的python文件名:")
	app = QtGui.QApplication(sys.argv)
	str = QtGui.QFileDialog.getOpenFileName(None, u"请选择Python文件", ".", "python Files(*.py);ALL (*.*)", None)
	if str != "" :
		setup(options=options, zipfile=None, console=[{"script": unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore')}])
		os.system("Explorer /select," + path + "dist\\" + unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore').split('/')[-1][:-3] + ".exe")
		pass
