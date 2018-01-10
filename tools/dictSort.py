#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-21 下午3:57
# @Author  : lilixiang
# @Site    : 
# @File    : dictSort.py
# @Software: PyCharm Community Edition
# 将字典按照参数名的字典排序，并将参数与参数值拼接为字符串,:参数1值1参数2值2....
import hashlib

def dictsort(Obj):
    arr = '';
    for key in sorted(Obj.keys()):
        # print(key)
        arr += key+str(Obj[key])
    return arr

def sha1(str2):
    s1 = hashlib.sha1()
    s1.update(str2.encode('utf-8'))
    return s1.hexdigest().lower()

def dictsorttosha1(Obj):
    return sha1(dictsort(Obj))