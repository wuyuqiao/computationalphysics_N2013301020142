import numpy as np
import math
from pylab import *

# define the function which do the calculation with correction

def with_cor(angle):

    # initialize

    x=[0.0]
    y=[0.0]
    vx=[700.0*np.cos(angle)]
    vy=[700.0*np.sin(angle)]
    v=[700.0]
    dt=0.02
    p1=4.0*pow(10.0,-5.0)
    p2=6.5*pow(10.0,-3.0)/280.0
    g=9.8
    alpha=2.5

    # calculate the trajectory

    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] - p1*pow(1-p2*y[-1],alpha)*v[-1]*vx[-1]*dt
        vy_new = vy[-1] - p1*pow(1-p2*y[-1],alpha)*v[-1]*vy[-1]*dt - g*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)

    # determine the land point

    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl

    # result

    return (x,y)

# define the function which do the calculation without correction 

def without_cor(angle):

    # initialize

    x=[0.0]
    y=[0.0]
    vx=[700.0*np.cos(angle)]
    vy=[700.0*np.sin(angle)]
    v=[700.0]
    dt=0.02
    p1=4.0*pow(10.0,-5.0)
    g=9.8

    # calculate the trajectory

    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] - p1*v[-1]*vx[-1]*dt
        vy_new = vy[-1] - p1*v[-1]*vy[-1]*dt - g*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)

    # determine the land point

    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl

    # result

    return (x,y)

# plot

x1 = array(with_cor(np.pi/4)[0])
y1 = array(with_cor(np.pi/4)[1])
x2 = array(with_cor(7*np.pi/36)[0])
y2 = array(with_cor(7*np.pi/36)[1])
x3 = array(without_cor(np.pi/4)[0])
y3 = array(without_cor(np.pi/4)[1])
x4 = array(without_cor(7*np.pi/36)[0])
y4 = array(without_cor(7*np.pi/36)[1])

plot(x1,y1,'y-',label='with density correction, 45 degree')
plot(x2,y2,'g-',label='with density correction, 35 degree')
plot(x3,y3,'r:',label='without density correction, 45 degree',linewidth=2.0)
plot(x4,y4,'b:',label='without density correction, 35 degree',linewidth=2.0)

grid(True)

title('Cannon shell trajectory')
xlabel('x(m)')
ylabel('y(m)')
xlim(0,35000)
ylim(0,12000)

legend(loc='upper right',frameon=False)

show()
