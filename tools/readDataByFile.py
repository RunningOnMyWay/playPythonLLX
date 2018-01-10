#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-8 下午4:38
# @Author  : lilixiang
# @Site    : 
# @File    : readDataByFile.py
# @Software: PyCharm Community Edition
from numpy import *
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines()) # get the number of lines in the file
    returnMat = zeros((numberOfLines, 3)) # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector