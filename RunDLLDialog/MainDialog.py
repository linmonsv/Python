# -*- coding: utf-8 -*-

"""
Module implementing DLLDialog.
"""

import sys
from ctypes import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import traceback
import ConfigParser
import os
import codecs

from Ui_MainDialog import Ui_Dialog


class DLLDialog(QtGui.QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    lResClass = []
    lReqClass = []

    def ReadStru_File(self, FileName="", lClass=[]):
        fp = open(FileName, "r")
        szcontext = ""
        lTemp = []
        while True:
            szcontext = fp.readline()
            szTemp = szcontext
            if szcontext and len(szcontext) > 5:
                print szcontext
                if szcontext.find("char") != -1:

                    szTemp = szTemp.replace("char", "").replace(" ", "").strip()
                    lTemp = []
                    if szTemp.find("[") == -1:
                        lTemp.append(szTemp[:szTemp.find(";")])
                        lTemp.append("1")
                        lTemp.append(szTemp[szTemp.find("/"):len(szTemp)])
                        pass
                    else:
                        lTemp.append(szTemp[:szTemp.find("[")])
                        lTemp.append(szTemp[szTemp.find("[") + 1:szTemp.find("]")])
                        lTemp.append(szTemp[szTemp.find("/"):len(szTemp)])
                        pass
                    lTemp.append("")
                    lClass.append(lTemp)
            elif szcontext and 5 >= len(szcontext):
                continue
            else:
                break
            pass
        pass

    def ReadStru_List(self, ListData=[], lClass=[]):
        szContext = ""
        lTemp = []
        for i in range(len(ListData)):
            szContext = ListData[i]
            szTemp = szContext
            if szContext and len(szContext) > 5:
                # print(szContext.decode("GBK")),
                if szContext.find("char") != -1:

                    szTemp = szTemp.replace("char", "").replace(" ", "").strip()
                    lTemp = []
                    if szTemp.find("[") == -1:
                        lTemp.append(szTemp[:szTemp.find(";")])
                        lTemp.append("1")
                        lTemp.append(szTemp[szTemp.find("/"):len(szTemp)])
                        pass
                    else:
                        lTemp.append(szTemp[:szTemp.find("[")])
                        lTemp.append(szTemp[szTemp.find("[") + 1:szTemp.find("]")])
                        lTemp.append(szTemp[szTemp.find("/"):len(szTemp)])
                        pass
                    lTemp.append("")
                    lClass.append(lTemp)
            elif szContext and 5 >= len(szContext):
                continue
            else:
                break
            pass
        pass

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.tableView_Res.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #self.tableView_Res.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.setWindowFlags(QtCore.Qt.Window)
        try :
            cf = ConfigParser.ConfigParser()
            bRet = os.path.exists('Config.ini')
            if bRet is False:
                fp = codecs.open('Config.ini', 'w', 'utf-8')
                cf.add_section("baseconf")
                cf.add_section("Request")
                cf.add_section("Response")
                cf.write(fp)
                fp.close()
                fp = codecs.open('Config.ini', 'w', 'utf-8')
                cf.set("baseconf", "AutoRead", "1")
                cf.set("baseconf", "DLLFile", "")
                cf.set("baseconf", "FunName", "")
                cf.set("Request", "Data", "")
                cf.set("Response", "Data", "")
                cf.set("Request", "Value", "")
                cf.set("Response", "Value", "")
                cf.write(fp)
                fp.close()
                pass
            else :
                cf.readfp(codecs.open("Config.ini", "r", "utf-8"))
                AutoRead = cf.get("baseconf", "AutoRead")
                DLLFile = cf.get("baseconf", "DLLFile")
                FunName = cf.get("baseconf", "FunName")
                StrRequest = cf.get("Request", "Data")
                StrRequestValue = cf.get("Request", "Value")
                StrResponse = cf.get("Response", "Data")
                if int(AutoRead) == 1:
                    self.lineEdit_DLL.setText(DLLFile)
                    self.lineEdit_FunName.setText(FunName)
                    self.lReqClass = []
                    self.lResClass = []

                    self.ReadStru_List(StrRequest.split('\n'), self.lReqClass)

                    modelReq = QtGui.QStandardItemModel()
                    modelReq.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
                    modelReq.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
                    modelReq.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
                    modelReq.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
                    self.tableView_Req.setModel(modelReq)
                    self.tableView_Req.setColumnWidth(0, 100)
                    self.tableView_Req.setColumnWidth(1, 100)
                    self.tableView_Req.setColumnWidth(2, 50)
                    self.tableView_Req.setColumnWidth(3, 500)

                    for i in range(len(self.lReqClass)):
                        modelReq.setItem(i, 0, QtGui.QStandardItem(self.lReqClass[i][0]))
                        modelReq.setItem(i, 2, QtGui.QStandardItem(self.lReqClass[i][1]))
                        modelReq.setItem(i, 3, QtGui.QStandardItem(self.lReqClass[i][2]))
                        pass
                    pass

                    self.ReadStru_List(StrResponse.split('\n'), self.lResClass)

                    modelRes = QtGui.QStandardItemModel()
                    modelRes.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
                    modelRes.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
                    modelRes.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
                    modelRes.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
                    self.tableView_Res.setModel(modelRes)
                    self.tableView_Res.setColumnWidth(0, 100)
                    self.tableView_Res.setColumnWidth(1, 100)
                    self.tableView_Res.setColumnWidth(2, 50)
                    self.tableView_Res.setColumnWidth(3, 500)

                    for i in range(len(self.lResClass)):
                        modelRes.setItem(i, 0, QtGui.QStandardItem(self.lResClass[i][0]))
                        modelRes.setItem(i, 2, QtGui.QStandardItem(self.lResClass[i][1]))
                        modelRes.setItem(i, 3, QtGui.QStandardItem(self.lResClass[i][2]))
                        pass
                    pass
                    print StrRequestValue
                    bOutputData = bytearray(StrRequestValue, 'GBK')
                    length = 1
                    for i in range(len(self.lReqClass)):
                        modelReq.setItem(i, 1, QtGui.QStandardItem(
                            str(bOutputData[length: length + int(self.lReqClass[i][1])]).decode('GBK')))
                        length += int(self.lReqClass[i][1])
                    pass
                pass

        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(None, u"错误", traceback.format_exc(),
                                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.
                                       QMessageBox.Yes);


    @QtCore.pyqtSignature("")
    def on_FindDLLButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            str = QtGui.QFileDialog.getOpenFileName(self, u"请选择DLL文件", ".", "DLL Files(*.DLL)", None)
            self.lineEdit_DLL.setText(str)
        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(None, u"错误", traceback.format_exc(),
                                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.
                                       QMessageBox.Yes);
            # raise NotImplementedError

    @QtCore.pyqtSignature("")
    def on_ReadResButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.lResClass = []
            str = QtGui.QFileDialog.getOpenFileName(self, u"请选择传出结构体文本文件", ".", "txt Files(*.txt)", None)
            if str == "":
                return
            cf = ConfigParser.ConfigParser()
            cf.read("Config.ini")
            fp = open(unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore').encode('GBK'), 'r');
            strAllData = fp.read()
            fp.close()
            print strAllData
            cf.set("Response", "Data", strAllData)
            fp = open("Config.ini", "w")
            cf.write(fp)
            fp.close()
            self.ReadStru_File(unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore').encode('GBK'), self.lResClass)
            print self.lResClass

            modelRes = QtGui.QStandardItemModel()
            modelRes.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
            modelRes.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
            modelRes.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
            modelRes.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
            self.tableView_Res.setModel(modelRes)
            self.tableView_Res.setColumnWidth(0, 100)
            self.tableView_Res.setColumnWidth(1, 100)
            self.tableView_Res.setColumnWidth(2, 50)
            self.tableView_Res.setColumnWidth(3, 500)

            for i in range(len(self.lResClass)):
                modelRes.setItem(i, 0, QtGui.QStandardItem(self.lResClass[i][0]))
                modelRes.setItem(i, 2, QtGui.QStandardItem(self.lResClass[i][1]))
                modelRes.setItem(i, 3, QtGui.QStandardItem(self.lResClass[i][2].decode('utf8')))
                pass
        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(None, u"错误", traceback.format_exc(),
                                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.
                                       QMessageBox.Yes);
            # raise NotImplementedError

    @QtCore.pyqtSignature("")
    def on_RunDLLButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            strInputData = ""
            strOutputData = ""
            if self.lineEdit_DLL.text() == "":
                QtGui.QMessageBox.critical(None, u"错误", u"DLL路径不得为空", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.
                                           QMessageBox.Yes);
                return
            if self.lineEdit_FunName.text() == "":
                QtGui.QMessageBox.critical(None, u"错误", u"DLL方法名不得为空", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.
                                           QMessageBox.Yes);
                return
            cf = ConfigParser.ConfigParser()
            cf.read("Config.ini")
            cf.set("baseconf", "DLLFile", unicode(QtCore.QString(self.lineEdit_DLL.text()).toUtf8(), 'utf8', 'ignore').encode('utf8'))
            cf.set("baseconf", "FunName", unicode(QtCore.QString(self.lineEdit_FunName.text()).toAscii()))
            fp = open("Config.ini", "w")
            cf.write(fp)
            fp.close()
            # 组织请求字符串
            ReqModel = self.tableView_Req.model()
            ResModel = self.tableView_Res.model()

            length = 0
            bInputTemp = bytearray()
            for k in range(len(self.lReqClass)):
                strInputData += ReqModel.data(ReqModel.index(k, 1)).toString()[0: int(self.lReqClass[k][1])]
                bInputTemp = bytearray(unicode(QtCore.QString(strInputData).toUtf8(), 'utf8', 'ignore'), 'GBK')
                length += int(self.lReqClass[k][1])
                ReqModel.setItem(k, 1, QtGui.QStandardItem(str(bInputTemp[length - int(self.lReqClass[k][1]): length]).decode('GBK')))
                # print unicode(QtCore.QString(strInputData).toUtf8(), 'utf8', 'ignore')
                if len(bInputTemp) < length:
                    strInputData += " " * (length - len(bInputTemp))
                    pass
                elif len(bInputTemp) > length :
                    print "超出字符串设置长度"
                    strInputData = strInputData[0: length - int(self.lReqClass[k][1])]
                    print str(bInputTemp[length - int(self.lReqClass[k][1]): length]).decode('GBK')
                    strInputData += QtCore.QString(str(bInputTemp[length - int(self.lReqClass[k][1]): length]).decode('GBK'))
                    pass

            bInputData = bytearray(unicode(QtCore.QString(strInputData).toUtf8(), 'utf8', 'ignore'), 'GBK')
            print "[" + bInputData + "]"
            self.textEdit.setText("")
            self.textEdit.append(u"入参字符串为:" + u"[" + str(len(bInputData)) + u"]\n[" + strInputData + u"]\n")

            strMsg = u"入参字符串为:" + u"[" + str(len(bInputData)) + u"]\n[" + strInputData + u"]\n"
            if QtGui.QMessageBox.question(None, u"提示", strMsg, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes) == QtGui.QMessageBox.No :
                return
            cf = ConfigParser.ConfigParser()
            cf.read("Config.ini")
            cf.set("Request", "Value", "[" + unicode(QtCore.QString(strInputData).toUtf8(), 'utf8', 'ignore').encode('utf8') + "]")
            fp = open("Config.ini", "w")
            cf.write(fp)
            fp.close()
            # 运行DLL
            strDLLName = ""
            strDLLName = unicode(QtCore.QString(self.lineEdit_DLL.text()).toUtf8(), 'utf8', 'ignore')
            dll = windll.LoadLibrary(strDLLName.encode('GBK'))
            strFuncName = unicode(QtCore.QString(self.lineEdit_FunName.text()).toUtf8(), 'utf8', 'ignore')
            strInputData = unicode(QtCore.QString(strInputData).toUtf8(), 'utf8', 'ignore').encode('GBK')
            strRequest = create_string_buffer(strInputData)
            strResponse = create_string_buffer(1024 * 10)
            pRequest = c_char_p()
            pResponse = c_char_p()
            pRequest.value = addressof(strRequest)
            pResponse.value = addressof(strResponse)

            strExec = "dll." + strFuncName + '(strRequest, addressof(strResponse))'
            print(strExec)
            print(eval(strExec))
            print(pResponse.value.decode("GBK"))
            strOutputData = pResponse.value.decode("GBK")
            bOutputData = bytearray(strOutputData, 'GBK')
            self.textEdit.append(u"出参字符串为\n:" + u"[" + str(len(bOutputData)) + u"]\n[" + strOutputData + u"]\n");

            strMsg = u"出参字符串为\n:" + u"[" + str(len(bOutputData)) + u"]\n[" + strOutputData + u"]\n"
            QtGui.QMessageBox.information(None, u"提示", strMsg, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            length = 0

            print len(bOutputData)
            for i in range(len(self.lResClass)):
                ResModel.setItem(i, 1, QtGui.QStandardItem(
                    str(bOutputData[length: length + int(self.lResClass[i][1])]).decode('GBK')))
                length += int(self.lResClass[i][1])
                pass
        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(None, u"错误", traceback.format_exc(),
                                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.
                                       QMessageBox.Yes);
            # raise NotImplementedError

    @QtCore.pyqtSignature("")
    def on_ReadReqButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.lReqClass = []
            str = QtGui.QFileDialog.getOpenFileName(self, u"请选择传入结构体文本文件", ".", "txt Files(*.txt)", None)
            if str == "":
                return
            cf = ConfigParser.ConfigParser()
            cf.read("Config.ini")
            fp = open(unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore').encode('GBK'), 'r');
            strAllData = fp.read()
            fp.close()
            print strAllData
            cf.set("Request", "Data", strAllData)
            fp = open("Config.ini", "w")
            cf.write(fp)
            fp.close()
            self.ReadStru_File(unicode(QtCore.QString(str).toUtf8(), 'utf8', 'ignore').encode('GBK'), self.lReqClass)
            print self.lReqClass

            modelReq = QtGui.QStandardItemModel()
            modelReq.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
            modelReq.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
            modelReq.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
            modelReq.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
            self.tableView_Req.setModel(modelReq)
            self.tableView_Req.setColumnWidth(0, 100)
            self.tableView_Req.setColumnWidth(1, 100)
            self.tableView_Req.setColumnWidth(2, 50)
            self.tableView_Req.setColumnWidth(3, 500)

            for i in range(len(self.lReqClass)):
                modelReq.setItem(i, 0, QtGui.QStandardItem(self.lReqClass[i][0]))
                modelReq.setItem(i, 2, QtGui.QStandardItem(self.lReqClass[i][1]))
                modelReq.setItem(i, 3, QtGui.QStandardItem(self.lReqClass[i][2].decode('utf8')))
                pass

        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(None, u"错误", traceback.format_exc(),
                                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.
                                       QMessageBox.Yes);
            # raise NotImplementedError

    @QtCore.pyqtSignature("QModelIndex")
    def on_tableView_Req_doubleClicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """

    @QtCore.pyqtSignature("QModelIndex")
    def on_tableView_Res_doubleClicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """

    @QtCore.pyqtSignature("")
    def on_ReadTXTReqButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.lReqClass = []
        strReq = self.textEdit.toPlainText()
        self.textEdit.setText("")
        print unicode(QtCore.QString(strReq).toUtf8(), 'utf8', 'ignore').split('\n')
        self.ReadStru_List(unicode(QtCore.QString(strReq).toUtf8(), 'utf8', 'ignore').split('\n'), self.lReqClass)
        cf = ConfigParser.ConfigParser()
        cf.read("Config.ini")
        cf.set("Request", "Data", unicode(QtCore.QString(strReq).toUtf8(), 'utf8', 'ignore').encode('utf8'))
        cf.set("Request", "Value", "")
        fp = open("Config.ini", "w")
        cf.write(fp)
        fp.close()
        modelReq = QtGui.QStandardItemModel()
        modelReq.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
        modelReq.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
        modelReq.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
        modelReq.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
        self.tableView_Req.setModel(modelReq)
        self.tableView_Req.setColumnWidth(0, 100)
        self.tableView_Req.setColumnWidth(1, 100)
        self.tableView_Req.setColumnWidth(2, 50)
        self.tableView_Req.setColumnWidth(3, 500)

        for i in range(len(self.lReqClass)):
            modelReq.setItem(i, 0, QtGui.QStandardItem(self.lReqClass[i][0]))
            modelReq.setItem(i, 2, QtGui.QStandardItem(self.lReqClass[i][1]))
            modelReq.setItem(i, 3, QtGui.QStandardItem(self.lReqClass[i][2]))
            pass

    @QtCore.pyqtSignature("")
    def on_ReadTXTResButton_clicked(self):
        """
        Slot documentation goes here.
        """

        self.lResClass = []
        strRes = self.textEdit.toPlainText()
        self.textEdit.setText("")
        print unicode(QtCore.QString(strRes).toUtf8(), 'utf8', 'ignore').split('\n')
        self.ReadStru_List(unicode(QtCore.QString(strRes).toUtf8(), 'utf8', 'ignore').split('\n'), self.lResClass)
        cf = ConfigParser.ConfigParser()
        cf.read("Config.ini")
        cf.set("Response", "Data", unicode(QtCore.QString(strRes).toUtf8(), 'utf8', 'ignore').encode('utf8'))
        fp = open("Config.ini", "w")
        cf.write(fp)
        fp.close()
        modelRes = QtGui.QStandardItemModel()
        modelRes.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"名称"))
        modelRes.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"内容"))
        modelRes.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"长度"))
        modelRes.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"注释"))
        self.tableView_Res.setModel(modelRes)
        self.tableView_Res.setColumnWidth(0, 100)
        self.tableView_Res.setColumnWidth(1, 100)
        self.tableView_Res.setColumnWidth(2, 50)
        self.tableView_Res.setColumnWidth(3, 500)

        for i in range(len(self.lResClass)):
            modelRes.setItem(i, 0, QtGui.QStandardItem(self.lResClass[i][0]))
            modelRes.setItem(i, 2, QtGui.QStandardItem(self.lResClass[i][1]))
            modelRes.setItem(i, 3, QtGui.QStandardItem(self.lResClass[i][2]))
            pass

    @QtCore.pyqtSignature("")
    def on_TXT2ResButton_clicked(self):
        """
        Slot documentation goes here.
        """
        strOutputData = unicode(self.textEdit.toPlainText())
        bOutputData = bytearray(strOutputData, 'GBK')

        length = 0
        ResModel = self.tableView_Res.model()
        for i in range(len(self.lResClass)):
                ResModel.setItem(i, 1, QtGui.QStandardItem(
                    str(bOutputData[length: length + int(self.lResClass[i][1])]).decode('GBK')))
                length += int(self.lResClass[i][1])
                pass

    @QtCore.pyqtSignature("")
    def on_TXT2ReqButton_clicked(self):
        """
        Slot documentation goes here.
        """
        strOutputData = unicode(self.textEdit.toPlainText())
        bOutputData = bytearray(strOutputData, 'GBK')

        length = 0
        ReqModel = self.tableView_Req.model()
        for i in range(len(self.lReqClass)):
                ReqModel.setItem(i, 1, QtGui.QStandardItem(
                    str(bOutputData[length: length + int(self.lReqClass[i][1])]).decode('GBK')))
                length += int(self.lReqClass[i][1])
                pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = DLLDialog()
    dlg.show()
    sys.exit(app.exec_())
    

