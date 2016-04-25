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
    dt = 0.01
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    

    # move the pendulum

    while t[-1] < 100:

        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)

        

        t_new = t[-1] + dt
        t.append(t_new)
        

    return angle,t


ang1 = change_amp(1.35)[0]
t1 = change_amp(1.35)[1]
ang2 = change_amp(1.44)[0]
t2 = change_amp(1.44)[1]
ang3 = change_amp(1.465)[0]
t3 = change_amp(1.465)[1]

figure()
plot(t1,ang1)
title('F=1.35')
xlabel('time(s)')
ylabel('theta(radians)')
grid(True)
xlim(0,100)

figure()
plot(t2,ang2)
title('F=1.44')
xlabel('time(s)')
ylabel('theta(radians)')
grid(True)
xlim(0,100)

figure()
plot(t3,ang3)
title('F=1.465')
xlabel('time(s)')
ylabel('theta(radians)')
grid(True)
xlim(0,100)



show()
