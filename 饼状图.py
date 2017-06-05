#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
labes=['A','B','C','D']
fracs=[15,30,45,10]
explode=[0,0.1,0.05,0]
#设置x,y轴比例为1：1，从而达到一个正的圆
plt.axes(aspect=1)
#labels标签参数,x是对应的数据列表,autopct显示每一个区域占的比例,explode突出显示某一块,shadow阴影
plt.pie(x=fracs,labels=labes,autopct="%.0f%%",explode=explode,shadow=True)
plt.show()

