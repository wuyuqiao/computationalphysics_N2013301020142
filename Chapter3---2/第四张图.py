from __future__ import division
from math import *
from pylab import *

# define a function that given amplitude of force, gives angle,avelo and t

def change_amp(theta0):
    
    # define some constants

    q = 0.5
    l = 9.8
    g = 9.8
    f = 2/3
    dt = 0.04
    F=0.5
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]

    # move the pendulum

    while t[-1] < 150:

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

angle_1 = change_amp(0.2)[0]
t = change_amp(0.2)[1]
angle_2 = change_amp(0.201)[0]
dtheta=[]
for i in range(len(angle_1)):
    dtheta.append(abs(angle_1[i-1]-angle_2[i-1]))

plot(t,dtheta)
semilogy(t,dtheta)


title('angle difference versus time')
xlabel('time(s)')
ylabel('angle difference(radians)')
xlim(0,150)
ylim(0,100)
grid(True)



show()
