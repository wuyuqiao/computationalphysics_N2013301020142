from __future__ import division
from numpy import *
from pylab import *

theta = [pi/4]
omega = [0]

t = [0]
q = 0.1
length = 1.0
g = 9.8
deltat = 0.04
force = 1
frequency = 10

while t[-1] <= 10:
    omega.append(omega[-1] - (g/length)*theta[-1] - q*omega[-1] + force*sin(frequency*t[-1]))
    theta.append(theta[-1] + omega[-1]*deltat)
    t.append(t[-1] + deltat)

theta_array = array(theta)
t_array = array(t)

plot(t_array,theta_array)

title('damped pendulum with driving force')
xlabel('time (s)')
ylabel('angle (radians)')
text(5,0.5,'frequency = 10,\n amplitude = 1, q=1',fontsize=15)

xlim(0,10)
ylim(-1,1)

grid(True)

show()
