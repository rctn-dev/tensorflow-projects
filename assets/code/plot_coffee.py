import numpy as np
from matplotlib import pyplot as plt

data=np.loadtxt('assets/data/coffe_data.txt')
X=data[:,[0,1]]
y=data[:,2]

fig=plt.figure(figsize=(4,3))
plt.scatter(X[y==0,0],X[y==0,1],marker='o',c='b')
plt.scatter(X[y==1,0],X[y==1,1],marker='x',c='r')
plt.xlabel('Temperature (C)')
plt.ylabel('Time Duration (min.)')
plt.legend(['0','1'])
plt.show()
