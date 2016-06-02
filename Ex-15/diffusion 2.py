import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def density(t_end):

    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    d = np.zeros((101,101))
    d[50][50]=1
    d1 = deepcopy(d)

    for t in range(t_end):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d

x,y,z = density(100)[0],density(100)[1],density(100)[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Distribution in 2 dimension, t=100')
plt.xlim(-50,50)
plt.ylim(-50,50)


plt.show()
    
