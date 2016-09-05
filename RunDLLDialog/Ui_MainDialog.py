# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Python\RunDLLDialog\MainDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(911, 448)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.FindDLLButton = QtGui.QPushButton(Dialog)
        self.FindDLLButton.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.FindDLLButton.setObjectName(_fromUtf8("FindDLLButton"))
        self.ReadResButton = QtGui.QPushButton(Dialog)
        self.ReadResButton.setGeometry(QtCore.QRect(650, 370, 121, 61))
        self.ReadResButton.setObjectName(_fromUtf8("ReadResButton"))
        self.RunDLLButton = QtGui.QPushButton(Dialog)
        self.RunDLLButton.setGeometry(QtCore.QRect(390, 370, 131, 61))
        self.RunDLLButton.setObjectName(_fromUtf8("RunDLLButton"))
        self.ReadReqButton = QtGui.QPushButton(Dialog)
        self.ReadReqButton.setGeometry(QtCore.QRect(140, 370, 121, 61))
        self.ReadReqButton.setObjectName(_fromUtf8("ReadReqButton"))
        self.lineEdit_FunName = QtGui.QLineEdit(Dialog)
        self.lineEdit_FunName.setGeometry(QtCore.QRect(632, 10, 261, 20))
        self.lineEdit_FunName.setObjectName(_fromUtf8("lineEdit_FunName"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(490, 10, 138, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(530, 43, 371, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(9, 43, 371, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_DLL = QtGui.QLineEdit(Dialog)
        self.lineEdit_DLL.setGeometry(QtCore.QRect(9, 10, 361, 20))
        self.lineEdit_DLL.setObjectName(_fromUtf8("lineEdit_DLL"))
        self.tableView_Req = QtGui.QTableView(Dialog)
        self.tableView_Req.setGeometry(QtCore.QRect(10, 60, 371, 301))
        self.tableView_Req.setObjectName(_fromUtf8("tableView_Req"))
        self.tableView_Res = QtGui.QTableView(Dialog)
        self.tableView_Res.setGeometry(QtCore.QRect(530, 60, 371, 301))
        self.tableView_Res.setObjectName(_fromUtf8("tableView_Res"))
        self.ReadTXTReqButton = QtGui.QPushButton(Dialog)
        self.ReadTXTReqButton.setGeometry(QtCore.QRect(10, 370, 121, 61))
        self.ReadTXTReqButton.setObjectName(_fromUtf8("ReadTXTReqButton"))
        self.ReadTXTResButton = QtGui.QPushButton(Dialog)
        self.ReadTXTResButton.setGeometry(QtCore.QRect(780, 370, 121, 61))
        self.ReadTXTResButton.setObjectName(_fromUtf8("ReadTXTResButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(390, 60, 131, 301))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(393, 40, 126, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.TXT2ResButton = QtGui.QPushButton(Dialog)
        self.TXT2ResButton.setGeometry(QtCore.QRect(530, 370, 111, 61))
        self.TXT2ResButton.setObjectName(_fromUtf8("TXT2ResButton"))
        self.TXT2ReqButton = QtGui.QPushButton(Dialog)
        self.TXT2ReqButton.setGeometry(QtCore.QRect(270, 370, 111, 61))
        self.TXT2ReqButton.setObjectName(_fromUtf8("TXT2ReqButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "测试DLL小工具", None))
        self.FindDLLButton.setText(_translate("Dialog", "浏览...", None))
        self.ReadResButton.setText(_translate("Dialog", "通过文本读取\n"
"返回结构体", None))
        self.RunDLLButton.setText(_translate("Dialog", "运行DLL", None))
        self.ReadReqButton.setText(_translate("Dialog", "通过文本读取\n"
"请求结构体", None))
        self.label.setText(_translate("Dialog", "需要运行DLL的方法名称：", None))
        self.label_3.setText(_translate("Dialog", "返回结构体", None))
        self.label_2.setText(_translate("Dialog", "请求结构体", None))
        self.ReadTXTReqButton.setText(_translate("Dialog", "通过字符串读取\n"
"请求结构体", None))
        self.ReadTXTResButton.setText(_translate("Dialog", "通过字符串读取\n"
"返回结构体", None))
        self.label_4.setText(_translate("Dialog", "字符串", None))
        self.TXT2ResButton.setText(_translate("Dialog", "将字符串转换为\n"
"返回结构体", None))
        self.TXT2ReqButton.setText(_translate("Dialog", "将字符串转换为\n"
"请求结构体", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

