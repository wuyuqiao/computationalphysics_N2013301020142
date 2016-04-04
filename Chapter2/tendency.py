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


# get some values of angles and ranges

angles = np.linspace(0,np.pi/2,90)
range_=[]

for i in angles:
    r=with_cor(i)[0][-1]
    range_.append(r)

range__=array(range_)

# plot

plot(angles,range__,'b-')
grid(True)

title('tendency between angle and range')
xlabel('angle')
xticks([0,np.pi/4,np.pi/2],[r'$0$',r'$+\pi/4$',r'$+\pi/2$'])
ylabel('range/m')
ylim(0,30000)

show()
