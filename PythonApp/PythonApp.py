# 安装指定国内镜像源
# pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install talib --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云 http://mirrors.aliyun.com/pypi/simple/
# 豆瓣(douban) http://pypi.douban.com/simple/
# 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
# 华中科技大学 http://pypi.hustunique.com/simple/  
# 山东大学 http://pypi.sdutlinux.org/simple/ 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
from talib import MA_Type
from moduleInputData import InputData

loadFile = InputData("Price.csv")


def main():
    print("hello world")
    print(loadFile.getFileName())

    print(loadFile.getContent())

    print(talib.SMA(loadFile.getClose()))
    #a = talib.EMA(real0, timeperiod = 100)
    #b = talib.EMA(real1, timeperiod = 100)
    upper, middle, lower = talib.BBANDS(loadFile.getClose(), matype=MA_Type.T3)
    #常见线的属性有：color,label,linewidth,linestyle,marker等
    plt.plot(upper, color='r', label='upper') #color='r'代表红色
    plt.plot(middle, color='b', label='middle') #color='r'代表红色
    plt.plot(lower, color='g', label='lower') #color='r'代表红色
    #plt.axis([0, 2*np.pi, -1, 1])#设置坐标范围axis([xmin,xmax,ymin,ymax])
    #plt.ylim(-1,1)#仅设置y轴坐标范围
    plt.show() #展示绘图
    #plt.figure()
    #plt.plot()
    #plt.show()
    return


if __name__ == '__main__':
   main()
