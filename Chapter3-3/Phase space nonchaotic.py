from __future__ import division
from pylab import *

# define the positions of z, r is variable
def phase(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.0001
    sigma=10
    b=8/3
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
    return x,y,z

figure()
subplot(1,2,1)
plot(phase(5)[0],phase(5)[2])
title('z vs x, r=5')
xlabel('x')
ylabel('z')
subplot(1,2,2)
plot(phase(10)[0],phase(10)[2])
title('z vs x, r=10')
xlabel('x')
ylabel('z')

show()
