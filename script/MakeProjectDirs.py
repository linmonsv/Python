__author__ = 'xwb'
# coding=utf-8

import os


def getpwd():
    path = os.getcwd()
    if path[len(path) - 1] != '\\':
        path += '\\'
        pass
    return path
    pass


if __name__ == '__main__':
    path = raw_input("请输入文件夹地址:")
    print path
    os.mkdir(path + "\\代码")
    os.mkdir(path + "\\文档")
    os.mkdir(path + "\\发布")
    pass
