#coding:utf-8
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
x=np.linspace(-10000,10000,100) #将-10到10等区间分成100份
y=x**2+x**3+x**7
plt.plot(x,y)
plt.show()

