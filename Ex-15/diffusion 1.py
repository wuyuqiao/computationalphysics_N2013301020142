import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def density(t_end):

    x = list(np.linspace(-50,50,101))
    d = list(np.zeros(50)) + list(np.ones(1)) + list(np.zeros(50))
    d1 = deepcopy(d)

    for i in range(t_end):
        for j in range(101):
            if j==0 or j==100:
                pass
            else:
                d[j] = 0.5* (d1[j+1] + d1[j-1])
        d1 = deepcopy(d)

    for i in range(101):
        if i==0 or i==100:
            pass
        else:
            if d[i]==0:
                d[i] = 0.5*(d1[i+1] + d1[i-1])
    return x, d

x1, d1 = density(0)[0], density(0)[1]
x2, d2 = density(10)[0], density(10)[1]
x3, d3 = density(100)[0], density(100)[1]

plt.plot(x1,d1,label='t=0')
plt.plot(x2,d2,label='t=10')
plt.plot(x3,d3,label='t=100')

plt.xlabel('x')
plt.ylabel('density')
plt.title('Diffusion in one dimension')
plt.xlim(-50,50)
plt.legend()

plt.show()

        
    

    
