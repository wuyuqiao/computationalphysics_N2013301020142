from __future__ import division
from numpy import *
from pylab import *

theta1 = [pi/4]
theta2 = [pi/4]
theta3 = [pi/4]
length = 1.0
g = 9.8
deltat = 0.04
omega1 = [0]
omega2 = [0]
omega3 = [0]
t1 = [0]
t2 = [0]
t3 = [0]
q1 = 0.1
q2 = 0.8
q3 = 1.0

while t1[-1] <= 10:
    omega1.append(omega1[-1] - (g/length)*theta1[-1] - q1*omega1[-1])
    theta1.append(theta1[-1] + omega1[-1]*deltat)
    t1.append(t1[-1] + deltat)

while t2[-1] <= 10:
    omega2.append(omega2[-1] - (g/length)*theta2[-1] - q2*omega2[-1])
    theta2.append(theta2[-1] + omega2[-1]*deltat)
    t2.append(t2[-1] + deltat)

while t3[-1] <= 10:
    omega3.append(omega3[-1] - (g/length)*theta3[-1] - q3*omega3[-1])
    theta3.append(theta3[-1] + omega3[-1]*deltat)
    t3.append(t3[-1] + deltat)

theta1_array = array(theta1)
theta2_array = array(theta2)
theta3_array = array(theta3)

t1_array = array(t1)
t2_array = array(t2)
t3_array = array(t3)

plot(t1_array,theta1_array,label='q=0.1')
plot(t2_array,theta2_array,label='q=0.8')
plot(t3_array,theta3_array,label='q=1.0')

legend(loc='upper right',frameon=True)

title('damped pendulum')
xlabel('time (s)')
ylabel('angle (radians)')

xlim(0,4)
ylim(-1,1)

grid(True)

show()
