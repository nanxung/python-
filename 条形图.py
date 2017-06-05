import matplotlib.pyplot as plt
import numpy as np
N=5
y=[20,10,30,25,15]
y1=np.random.randint(10,50,5)
x=np.random.randint(10,1000,N)
index=np.arange(N)
# plt.bar(left=index,height=y,color='red',width=0.3)
# plt.bar(left=index+0.3,height=y1,color='black',width=0.3)
#plt.barh() 加了h就是横向的条形图，不用设置orientation
plt.bar(left=0,bottom=index,width=y,color='red',height=0.5,orientation='horizontal')
plt.show()