from __future__ import division
from visual import *

support = box(pos=vector(0,1,0),size=(1,0.01,1),material=materials.wood,color=color.green)
pendulum = sphere(radius=0.05,material=materials.wood,color=color.red)
pendulum.theta = pi/4
l = 1
g=9.8
deltat = 0.04
pendulum.omega = 0
pendulum.pos = vector(l*sin(pendulum.theta),1-l*cos(pendulum.theta),0)
string = curve(pos=[support.pos, pendulum.pos])

while True:
    rate(1/deltat)
    pendulum.omega -= (g/l)*pendulum.theta*deltat
    pendulum.theta += pendulum.omega*deltat
    pendulum.pos = vector(l*sin(pendulum.theta),1-l*cos(pendulum.theta),0)
    string.pos = [support.pos, pendulum.pos]
    
