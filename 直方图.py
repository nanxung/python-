#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

# m1=100
# sigma=20
# x=m1+sigma*np.random.randn(2000)
# plt.hist(x,bins=50,color="green",normed=True)
# plt.show()

#双变量的直方图
#颜色越深频率越高
#研究双变量的联合分布
x=np.random.rand(1000)+2
y=np.random.rand(1000)+3
plt.hist2d(x,y,bins=40)
plt.show()
