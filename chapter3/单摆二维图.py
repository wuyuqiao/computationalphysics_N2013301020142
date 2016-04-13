from __future__ import division
from numpy import *
from pylab import *

theta_first = [pi/4]
theta_second = [pi/2]
theta_third = [pi/8]
length = 1.0
g = 9.8
deltat = 0.04
omega_first = [0]
omega_second = [0]
omega_third = [0]
t_first = [0]
t_second = [0]
t_third = [0]

while t_first[-1] <= 10:
    omega_first.append(omega_first[-1] - (g/length)*theta_first[-1]*deltat)
    theta_first.append(theta_first[-1] + omega_first[-1]*deltat)
    t_first.append(t_first[-1] + deltat)

while t_second[-1] <= 10:
    omega_second.append(omega_second[-1] - (g/length)*theta_second[-1]*deltat)
    theta_second.append(theta_second[-1] + omega_second[-1]*deltat)
    t_second.append(t_second[-1] + deltat)

while t_third[-1] <= 10:
    omega_third.append(omega_third[-1] - (g/length)*theta_third[-1]*deltat)
    theta_third.append(theta_third[-1] + omega_third[-1]*deltat)
    t_third.append(t_third[-1] + deltat)


theta_first_array = array(theta_first)
t_first_array = array(t_first)

theta_second_array = array(theta_second)
t_second_array = array(t_second)

theta_third_array = array(theta_third)
t_third_array = array(t_third)

plot(t_first_array,theta_first_array,label='the origin of theta is pi/4')
plot(t_second_array,theta_second_array,label='the origin of theta is pi/2')
plot(t_third_array,theta_third_array,label='the origin of theta is pi/8')

title('Simple Pendulum - Euler-Cormer method')
xlabel('time (s)')
ylabel('angle (radians)')

legend(loc='upper right',frameon = True)

xlim(0,10)
ylim(-4,4)

grid(True)

show()
