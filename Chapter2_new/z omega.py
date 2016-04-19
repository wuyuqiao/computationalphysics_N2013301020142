from __future__ import division
from numpy import *
from pylab import *
from math import *

# define drag coefficient of normal ball
def normal(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=150:
        return -0.003*x+0.65
    if x>150:
        return 0.2

def data(ox,oy,oz):
    
    x0 = 0
    y0 = 1
    z0 = 0
    theta = [pi/4]
    velo = [100]
    velox = [velo[0]*cos(theta[0])]
    veloy = [velo[0]*sin(theta[0])]
    veloz = [0]
    x = [x0]
    y = [y0]
    z = [z0]
    deltat = 0.01
    g = 9.8

    while y[-1] >= 0:

        co = 1/(3.6**2)
        velox_add = velox[-1] - co*normal(3.6*velo[-1])*velo[-1]*velox[-1]*deltat + 0.00041*(oy*veloz[-1]-oz*veloy[-1])*deltat
        veloy_add = veloy[-1] - co*normal(3.6*velo[-1])*velo[-1]*veloy[-1]*deltat + 0.00041*(oz*velox[-1]-ox*veloz[-1])*deltat - g*deltat
        veloz_add = veloz[-1] - co*normal(3.6*velo[-1])*velo[-1]*veloz[-1]*deltat + 0.00041*(ox*veloy[-1]-oy*velox[-1])*deltat
        velo_add = sqrt((velox_add)**2+(veloy_add)**2+(veloz_add)**2)
        velox.append(velox_add)
        veloy.append(veloy_add)
        veloz.append(veloz_add)
        velo.append(velo_add)
        x.append(x[-1]+velox[-1]*deltat)
        y.append(y[-1]+veloy[-1]*deltat)
        z.append(z[-1]+veloz[-1]*deltat)

    if y[-1] <0:
        r = -y[-2]/y[-1]
        xl = (x[-2]+r*x[-1])/(r+1)
        x[-1] = xl
        y[-1] = 0

    return x,y,z

x1,y1,z1 = array(data(0,0,0)[0]),array(data(0,0,0)[1]),array(data(0,0,0)[2])
x2,y2,z2 = array(data(0,100,0)[0]),array(data(0,100,0)[1]),array(data(0,100,0)[2])
x3,y3,z3 = array(data(0,500,0)[0]),array(data(0,500,0)[1]),array(data(0,500,0)[2])
x4,y4,z4 = array(data(0,1000,0)[0]),array(data(0,1000,0)[1]),array(data(0,1000,0)[2])
x5,y5,z5 = array(data(0,2000,0)[0]),array(data(0,2000,0)[1]),array(data(0,2000,0)[2])

figure()
subplot(2,1,1)

plot(x1,y1,label='angular velocity = 0 rps')
plot(x2,y2,label='angular velocity = 100 rps')
plot(x3,y3,label='angular velocity = 500 rps')
plot(x4,y4,label='angular velocity = 1000 rps')
plot(x5,y5,label='angular velocity = 2000 rps')

legend(loc='right')
title('up:X-Y: horizontal and vertical.down:X-Z both horizontal')
xlabel('x /m')
ylabel('y /m')
grid(True)
ylim(0,100)
xlim(0,200)


subplot(2,1,2)

plot(x1,z1,label='angular velocity = 0 rps')
plot(x2,z2,label='angular velocity = 50 rps')
plot(x3,z3,label='angular velocity = 100 rps')
plot(x4,z4,label='angular velocity = 200 rps')
plot(x5,z5,label='angular velocity = 300 rps')

legend(loc='right')

xlabel('x /m')
ylabel('z /m')
grid(True)
ylim(-50,0)
xlim(0,200)


show()
