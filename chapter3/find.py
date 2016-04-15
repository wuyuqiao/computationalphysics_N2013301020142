from __future__ import division
from numpy import *
from pylab import *

def find_period(theta):

    theta1 = [theta]
    omega1 = [0]
    t1 = [0]
    length = 1
    g = 9.8
    deltat1 = 0.00001

    while t1[-1] <= 10:
        omega1.append(omega1[-1] - (g/length)*sin(theta1[-1]))
        theta1.append(theta1[-1] + omega1[-1]*deltat1)
        t1.append(t1[-1] + deltat1)

    count=[]
    for i in t1:
        if len(count) > 2:
            break
        if t1.index(i) == 0 or t1.index(i) == len(t1)-1:
            continue
        if theta1[t1.index(i)] > theta1[t1.index(i)+1] and theta1[t1.index(i)] > theta1[t1.index(i)-1]:
            count.append(i)

    period = count[1]-count[0]

    return period

th = linspace(pi/100,pi/2,100)

pe = []
for i in th:
    pe.append(find_period(i))

pe_one = [find_period(pi/100)]*len(pe)

plot(th,pe,label='nonlinear pendulum')
plot(th,pe_one,label='linear pendulum')

legend(loc='upper left',frameon=True)


xlim(pi/100,pi/2)
title('Relation between initial angle and period')
xlabel('initial angle(radians)')
ylabel('period(s)')
grid(True)

show()
