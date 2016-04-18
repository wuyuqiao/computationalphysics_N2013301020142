from __future__ import division
from numpy import *
from pylab import *
from math import *

# define drag coefficient of smooth ball
def smooth(x):

    if 0<=x<=150:
        return 0.5
    if 150<=x<=200:
        return -0.008*x+1.7
    if x>200:
        return 0.1

# define drag coefficient of normal ball
def normal(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=150:
        return -0.003*x+0.65
    if x>150:
        return 0.2

# define drag coefficient of rough ball
def rough(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=70:
        return -0.02*x+1.5
    if 70<=x<=120:
        return 0.004*x-0.18
    if x>120:
        return 0.3

def data(D):
    
    x0 = 0
    y0 = 1
    theta = [pi/4]
    velo = [30.56]
    velox = [velo[0]*cos(theta[0])]
    veloy = [velo[0]*sin(theta[0])]
    x = [x0]
    y = [y0]
    deltat = 0.01
    g = 9.8

    while y[-1] >= 0:

        co = 1/(3.6**2)
        velox.append(velox[-1]-((co*D(3.6*velo[-1])*velo[-1]*velox[-1])*deltat))
        veloy.append(veloy[-1]-(g+co*D(3.6*velo[-1])*velo[-1]*veloy[-1])*deltat)
        velo.append(sqrt((velox[-1])**2+(veloy[-1])**2))
        x.append(x[-1]+velox[-1]*deltat)
        y.append(y[-1]+veloy[-1]*deltat)

    if y[-1] <0:
        r = -y[-2]/y[-1]
        xl = (x[-2]+r*x[-1])/(r+1)
        x[-1] = xl
        y[-1] = 0

    return x,y
        
xs = array(data(smooth)[0])
ys = array(data(smooth)[1])
xn = array(data(normal)[0])
yn = array(data(normal)[1])
xr = array(data(rough)[0])
yr = array(data(rough)[1])

plot(xs,ys,label='smooth ball')
plot(xn,yn,label='normal ball')
plot(xr,yr,label='rough ball')

legend(loc='upper right')
title('different ball')
xlabel('x(m)')
ylabel('y(m)')
grid(True)

show()








        

