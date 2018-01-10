# playPythonLLX
just for learning

# python3.5

# need lib 
## 1. numpy
     1.1 获取从文件中逐行获取数据
        示例
            from numpy import *
            from  sampledatas.gradedata import creatematrixdata

            group,labels = creatematrixdata("sampledatas/dataForKNN.txt",3)
            print(group[0:10],labels[0:10])
         打印结果：
            [[  4.09200000e+04   8.32697600e+00   9.53952000e-01]
             [  1.44880000e+04   7.15346900e+00   1.67390400e+00]
             [  2.60520000e+04   1.44187100e+00   8.05124000e-01]
             [  7.51360000e+04   1.31473940e+01   4.28964000e-01]
             [  3.83440000e+04   1.66978800e+00   1.34296000e-01]
             [  7.29930000e+04   1.01417400e+01   1.03295500e+00]
             [  3.59480000e+04   6.83079200e+00   1.21319200e+00]
             [  4.26660000e+04   1.32763690e+01   5.43880000e-01]
             [  6.74970000e+04   8.63157700e+00   7.49278000e-01]
             [  3.54830000e+04   1.22731690e+01   1.50805300e+00]] [3, 2, 1, 1, 1, 1, 3, 3, 1, 3]

## 2. BeautifulSoup

## 3. urlopen

## 4. matplotlib

## 5. python3-tk
    sudo apt-get install python3-tk

