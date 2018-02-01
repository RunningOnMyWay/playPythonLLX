#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-2-1 上午10:37
# @Author  : lilixiang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm Community Edition
import sys

names = ['llx','Albert','Jack'];
passwords = ['123','ljh','saa'];

i = 0
name = ''
while name not in names:
    print("please input your name "+("again" if i>0 else "")+":")
    name = input()
    i +=1
    if i>10:
        sys.exit() # 直接结束程序
print('Thank You , '+name)
psw = ''
auth = True
while psw != passwords[names.index(name)]:
    print("please type right password:")
    psw = input()
    if(psw == 'exit'):
        auth = not auth
        break
if auth:
    print('welcome back , '+name)
else:
    print('Thank You for your trying!')
