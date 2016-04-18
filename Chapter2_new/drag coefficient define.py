import numpy as np
from pylab import *

# define drag coefficient of smooth ball
def smooth(x):

    if 0<=x<=150:
        return 0.5
    if 150<=x<=200:
        return -0.008*x+1.7
    if x>200:
        return 0.1

# define drag coefficient of normal ball
def normal(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=150:
        return -0.003*x+0.65
    if x>150:
        return 0.2

# define drag coefficient of rough ball
def rough(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=70:
        return -0.02*x+1.5
    if 70<=x<=120:
        return 0.004*x-0.18
    if x>120:
        return 0.3

# draw

v = list(np.linspace(0,300,300))

d1 = []
d2 = []
d3 = []

for i in v:
    d1.append(smooth(i))
    d2.append(normal(i))
    d3.append(rough(i))

x = array(v)
y1 = array(d1)
y2 = array(d2)
y3 = array(d3)
    
plot(x,y1,label='smooth ball')
plot(x,y2,label='normal ball')
plot(x,y3,label='rough ball')
legend(loc='upper right',frameon=True)
grid(True)

title('drag coefficient of different kind of balls')
xlabel('v (miles per hour)')
ylabel('Drag Coefficient')
xlim(0,300)
ylim(0,0.6)

show()

        
