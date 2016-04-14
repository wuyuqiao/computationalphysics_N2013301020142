from __future__ import division
from numpy import *
from pylab import *

theta1 = [pi/2]
omega1 = [0]
t1 = [0]
theta2 = [pi/16]
omega2 = [0]
t2 = [0]

length = 1.0
g = 9.8
deltat1 = 0.01
deltat2 = 0.01

while t1[-1] <= 1:
    omega1.append(omega1[-1] - (g/length)*sin(theta1[-1]))
    theta1.append(theta1[-1] + omega1[-1]*deltat1)
    t1.append(t1[-1] + deltat1)

while t2[-1] <= 1:
    omega2.append(omega2[-1] - (g/length)*sin(theta2[-1]))
    theta2.append(theta2[-1] + omega2[-1]*deltat2)
    t2.append(t2[-1] + deltat2)


plot(t1,theta1)
plot(t2,theta2)

title('nonlinear pendulum')
xlabel('time(s)')
ylabel('angle(radians)')
grid(True)

xlim(0,1)


show()
