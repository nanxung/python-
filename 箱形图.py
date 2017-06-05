#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
data=np.random.normal(loc=0,scale=1,size=1000)
#sym 点的形状，whis虚线的长度
plt.boxplot(data,sym="o",whis=1.5)
plt.show()
