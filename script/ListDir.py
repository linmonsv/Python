# -*- coding: utf-8 -*-
import os
import sys
import configparser


def list(path, dirlist=[]):
    fileobj = os.listdir(path)
    for f in fileobj:
        if (os.path.isdir(path + '/' + f)):
            dirlist.append(f)
            pass
        pass
    pass


if __name__ == "__main__":
    path = raw_input(u"请输入想要说明的路径:".encode("GBK"))
    # path = os.getcwd()
    cf = configparser.ConfigParser()
    dirlist = []
    print(path[len(path) - 1] != '\\')
    if path[len(path) - 1] != '\\':
        path += '\\'
        pass
    print(path)

    list(path, dirlist)
    ###	fp = open(path + u'说明.txt'.encode("GBK"), 'w')
    cf.read(path + '说明.txt')
    for i in range(len(dirlist)):
        print(dirlist[i])
        if (dirlist[i] not in cf.sections()):
            temp = "此代码取自" + ": \n" + "版本" + ": \n"
            cf.add_section(dirlist[i])
            cf.set(dirlist[i], temp, "")
        ###		fp.write(dirlist[i] + "\n")
        ###		fp.write(u"此代码取�?.encode("GBK") + ": \n")
        ###		fp.write(u"版本".encode("GBK") + ": \n")
        ###		fp.write("\n")
        pass
    cf.write(open(path + '说明.txt', "w"))
