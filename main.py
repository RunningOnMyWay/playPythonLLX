#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-20 上午10:32
# @Author  : lilixiang
# @Site    : 
# @File    : main.py
# @Software: PyCharm Community Edition

#8 12306 查询车票数据
from urllib.request import urlopen
import json
res = urlopen("https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-10&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NFF&purpose_codes=ADULT")
print(res.read().decode('utf-8','ignore'))
print(res.read())
data = json.dumps(res.read().decode('utf-8','ignore'))
print(data)
# print(data['data'])




# 7 将图像转化为二维向量，并转换红蓝像素

# import matplotlib.pyplot as plt # plt 用于显示图片
# import matplotlib.image as mpimg # mpimg 用于读取图片
# import numpy as np
# import os
#
#
# # 无法使用相对路径，因此使用绝对的文件路径
# lena = mpimg.imread(os.path.dirname(os.path.realpath(__file__))+'/sampledatas/america.png') # 读取和代码处于同一目录下的 lena.png
# # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
#
# lena.shape #(512, 512, 3)
#
# plt.imshow(lena) # 显示图片
# # plt.axis('off') # 不显示坐标轴
# # plt.show()
#
# lena_1 = lena[:,:,1]
# print(lena_1[0:12])
# plt.imshow(lena_1)
# plt.show()


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# html = urlopen("http://blog.csdn.net/hy245120020/article/details/50776197")
# bsObj = BeautifulSoup(html,"html.parser")

# 1获取地址中h2标签中id属性包含“virtualenv”的所有h2的html内容/文本内容/属性id值
# h1s = bsObj.findAll("h2",{"id":re.compile("virtualenv")})
# for h1 in h1s:
#     print(h1)
#     print(h1.get_text())
#     print(h1.attrs["id"])

# 2 获取代码中有制定个数属性的标签
# tags = bsObj.findAll(lambda tag: len(tag.attrs) ==1)
# for tag in tags:
#     print(tag)

# 3 签名
# from tools.dictSort import dictsorttosha1
# d = {"timestamp":5022410,"appkey":"asdasdsad","version":"1.0","secret":"asdasdasdasdasd","boolean":"true"}
# print(dictsorttosha1(d)) #获取按参数字典排序的参数1值1参数2值2..方式的字符串


# 4 采集整站
# pages = set()
#
#
# def getlinks(pageurl):
#     global pages
#     html = urlopen("http://www.juxian.com"+pageurl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     for link in  bsObj.findAll("a"):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getlinks(newPage)
# getlinks("/m/a/index.html")


# 5  k-近邻算法
# from numpy import *
# import operator
# from  sampledatas.gradedata import createDataSet
# group, labels = createDataSet()

# inX 用于分类的输入向量  dataSet 训练样本集合 labels 标签向量 k K-近邻算法中的k
# shape array的属性，描述一个多维数组的深度
# tile(inX, (dataSetSize,1)) 把inX二维数组化，dataSetSize表示生成数组后的行数，1表示列的倍数。整个这一行代码表示前一个二维数组矩阵的
# 每一个元素减去后一个数组对应的元素值，这样就实现了矩阵之间的减法
# axis=1：参数等于1的时候，表示矩阵中行之间的数的求和，等于0的时候表示列之间数的求和。
# argsort()：对一个数组进行非降序排序
# classCount.get(numOflabel,0) + 1：这一行代码不得不说的确很精美啊。get()：该方法是访问字典项的方法，即访问下标键为numOflabel的项，
# 如果没有这一项，那么初始值为0。然后把这一项的值加1。所以Python中实现这样的操作就只需要一行代码，实在是很简洁高效。
# 在python3.5 中的 字典中没有了iteritems方法属性，现在是items方法

# def classify(inX, dataSet, labels, k):
#     dataSetSize = dataSet.shape[0]
#     diffMat = tile(inX, (dataSetSize,1)) - dataSet
#     sqDiffMat = diffMat**2
#     sqDistances = sqDiffMat.sum(axis=1)
#     distances = sqDistances**0.5
#     sortedDistances = distances.argsort()
#     classCount = {}
#     for i in range(k):
#         numOflabel = labels[sortedDistances[i]]
#         classCount[numOflabel] = classCount.get(numOflabel,0) + 1
#     sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
#     return sortedClassCount[0][0]
#
# my = classify([59,0], group, labels, 1)
# print(my)



# 6 Python数据可视化——使用Matplotlib创建散点图

# from numpy import *
# import numpy as np
# from  sampledatas.gradedata import creatematrixdata
# import matplotlib
# from matplotlib import pyplot
#
# group,labels = creatematrixdata("sampledatas/dataForKNN.txt",3)
# print(group[0:10],labels[0:10])
# zhfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')
# fig = pyplot.figure()
#     # pyplot.xlabel(u'Test横轴X',fontproperties=zhfont)
#     # pyplot.ylabel(u'Test纵轴Y',fontproperties=zhfont)
# ax = pyplot.subplot(111)
#     # ax.scatter(group[:,1],group[:,2],15.0*array(labels),15.0*array(labels))
# labels = np.array(labels)
#     # print(labels[0:6])
# idx_1 = np.where(labels==1)
# p1 = ax.scatter(group[idx_1,0],group[idx_1,1],marker="_",color="r",label='1',s=20)
# idx_2 = np.where(labels==2)
# p2 = ax.scatter(group[idx_2,0],group[idx_2,1],marker="+",color="y",label='2',s=20)
# idx_3 = np.where(labels==3)
# p3 = ax.scatter(group[idx_3,0],group[idx_3,1],marker="*",color="g",label='3',s=20)
# pyplot.xlabel(u'每年的飞行里程数',fontproperties=zhfont)
# pyplot.ylabel(u'玩视频游戏所消耗的事件百分比',fontproperties=zhfont)
# ax.legend((p1,p2,p3),(u'不喜欢',u'一般',u'超爱'),loc = 2,prop=zhfont)
#
# pyplot.show()


