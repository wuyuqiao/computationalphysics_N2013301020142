from __future__ import division
from math import *
from pylab import *

# define a function that given amplitude of force, gives angle,avelo and t

def change_amp(F):
    
    # define some constants

    q = 0.5
    l = 9.8
    g = 9.8
    f = 2/3
    dt = pi/100
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    an=[theta0]
    av=[omega0] 

    # move the pendulum

    while t[-1] < 6000*pi:

        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)

        if t[-1]%(3*pi) <= dt:
            an.append(angle_new)
            av.append(avelo_new)

        t_new = t[-1] + dt
        t.append(t_new)
        

    return an,av


ang1 = change_amp(1.2)[0]
ave1 = change_amp(1.2)[1]
ang2 = change_amp(1.25)[0]
ave2 = change_amp(1.25)[1]
ang3 = change_amp(1.3)[0]
ave3 = change_amp(1.3)[1]


subplot(1,3,1)
scatter(ang1,ave1,s=10)
title('F=1.2')
xlabel('theta(radians)')
ylabel('omega(radians/s)')
grid(True)

subplot(1,3,2)
scatter(ang2,ave2,s=10)
title('F=1.25')
xlabel('theta(radians)')
ylabel('omega(radians/s)')
grid(True)

subplot(1,3,3)
scatter(ang3,ave3,s=10)
title('F=1.3')
xlabel('theta(radians)')
ylabel('omega(radians/s)')
grid(True)



show()
