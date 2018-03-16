#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-16 上午11:28
# @Author  : lilixiang
# @Site    : 
# @File    : ticTacToe.py
# @Software: PyCharm Community Edition
# 九宫格
jiaozhiban = {'top-L':'*','top-M':'*','top-R':'*','mid-L':'*','mid-M':'*','mid-R':'*','low-L':'*','low-M':'*','low-R':'*'}

def printJiaozhiban(jiaozhiban):
    print(jiaozhiban['top-L']+'|'+jiaozhiban['top-M']+'|'+jiaozhiban['top-R'])
    print(jiaozhiban['mid-L'] + '|' + jiaozhiban['mid-M'] + '|' + jiaozhiban['mid-R'])
    print(jiaozhiban['low-L'] + '|' + jiaozhiban['low-M'] + '|' + jiaozhiban['low-R'])

player = "X"
for i in range(9):
    printJiaozhiban(jiaozhiban)
    print("Turn for player "+player+" move on which space?")
    move = input()
    if move in jiaozhiban.keys() and jiaozhiban[move] == '*':
        jiaozhiban[move] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        print(jiaozhiban)
    else:
        print("Turn for player "+player+" move error?")
        i-=1