#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-4 下午5:42
# @Author  : lilixiang
# @Site    : 
# @File    : gradedata.py
# @Software: PyCharm Community Edition


# 分数等级二维样本数据
from numpy import *
import operator
def createDataSet():
    group = array([[0,0],[20,0],[55,0],[59,0],[60,0],[69,0],[75,0],[79,0],[80,0],[89,0],[90,0],[99,0],[100,0]])
    labels = ['E','E','E','E','C','C','C','C','B','B','A','A','A+']
    return group,labels

# 数据文件 /sampledatas/dataForKNN.txt
# 前num列为样本数据，最后一列为类型
def creatematrixdata(filepath,num):
    openfile = open(filepath).readlines()
    numoflines = len(openfile)  #得到行数
    returnMatrix = zeros((numoflines,num))  #返回来一个给定形状和类型的用0填充的数组
    classLabelVector = [] #准备返回标签
    index = 0
    for line in openfile:
        line = line.strip()
        lineFromLine = line.split("\t")
        returnMatrix[index,:] = lineFromLine[0:num]
        classLabelVector.append(int(lineFromLine[-1]))
        index += 1
    return returnMatrix,classLabelVector