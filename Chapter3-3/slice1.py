from __future__ import division
from pylab import *

def phase_yz(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.001
    sigma=10
    b=8/3
    y0=[]
    z0=[]
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
        if t[-1]>30:
            if abs(x[-1])<0.01:
                y0.append(y[-1])
                z0.append(z[-1])
    return y0,z0

def phase_xz(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.001
    sigma=10
    b=8/3
    x0=[]
    z0=[]
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
        if t[-1]>30:
            if abs(y[-1])<0.01:
                x0.append(x[-1])
                z0.append(z[-1])
    return x0,z0

subplot(1,2,1)
y0=phase_yz(25)[0]
z0=phase_yz(25)[1]
scatter(y0,z0,s=0.1)
title('z vs y when x=0')
xlabel('y')
ylabel('z')
xlim(-10,10)
ylim(0,30)

subplot(1,2,2)
x00=phase_xz(25)[0]
z00=phase_xz(25)[1]
scatter(x00,z00,s=0.1)
title('z vs x when y=0')
xlabel('x')
ylabel('z')
xlim(-20,20)
ylim(0,40)

show()

    

    
    


