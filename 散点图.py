#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
N=50
# height=np.random.randint(150,180,20)
# weight=np.random.randint(80,150,20)
x=np.random.randn(N)
y=np.random.randn(N)
plt.scatter(x,y,s=50,c='r',marker='o',alpha=0.5)
plt.show()

