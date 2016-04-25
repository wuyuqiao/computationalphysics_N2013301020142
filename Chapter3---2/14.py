from __future__ import division
from math import *
from pylab import *
from numpy import *

# define a function that given amplitude of force, gives angle,avelo and t

def change_amp(F,f):
    
    # define some constants

    q = 0.5
    l = 9.8
    g = 9.8
    dt = pi/100
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    an=[]
    

    # move the pendulum

    while t[-1] <= 1200*pi:

        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)
        if t[-1]>=900*pi:
            if t[-1]%(3*pi)<=dt:
                an.append(angle_new)
        t_new = t[-1] + dt
        t.append(t_new)
        

    return an
###

fdd_1=list(linspace(1.35,1.5,100))
fd_1=[]
th_1=[]

for i in fdd_1:
    points=change_amp(i,2/3)
    for j in points:
        fd_1.append(i)
        th_1.append(j)
###
        
fdd_2=list(linspace(1.35,1.5,100))
fd_2=[]
th_2=[]

for i in fdd_2:
    points=change_amp(i,2/3+0.00001)
    for j in points:
        fd_2.append(i)
        th_2.append(j)
###
        
fdd_3=list(linspace(1.35,1.5,100))
fd_3=[]
th_3=[]

for i in fdd_3:
    points=change_amp(i,2/3+0.00002)
    for j in points:
        fd_3.append(i)
        th_3.append(j)

###
subplot(1,3,1)
scatter(fd_1,th_1,s=10)
grid(True)
xlim(1.35,1.48)
ylim(0,3)
title('f=2/3')
xlabel('FD')
ylabel('theta(radians)')

subplot(1,3,2)
scatter(fd_2,th_2,s=10)
grid(True)
xlim(1.35,1.48)
ylim(0,3)
title('f=(2/3)+0.00001')
xlabel('FD')
ylabel('theta(radians)')

subplot(1,3,3)
scatter(fd_3,th_3,s=10)
grid(True)
xlim(1.35,1.48)
ylim(0,3)
title('f=(2/3)+0.00002')
xlabel('FD')
ylabel('theta(radians)')

show()









        
    


