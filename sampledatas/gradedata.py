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