from __future__ import division
from pylab import *

# define the positions of z, r is variable
def z(r):
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
    return t,z

figure()

subplot(2,1,1)
plot(z(160)[0],z(160)[1])
title('up:r=160,down:r=163.8')
xlabel('time(s)')
ylabel('z')
xlim(0,30)
ylim(0,310)
grid(True)

subplot(2,1,2)
plot(z(163.8)[0],z(163.8)[1])

xlabel('time(s)')
ylabel('z')
xlim(0,30)
ylim(0,310)
grid(True)



show()
