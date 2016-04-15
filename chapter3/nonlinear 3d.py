from __future__ import division
from visual import *

support1 = box(pos=vector(0,1,1),size=(1,0.01,1),material=materials.wood,color=color.red)
support2 = box(pos=vector(0,1,0),size=(1,0.01,1),material=materials.wood,color=color.green)

pendulum1 = sphere(radius=0.05,material=materials.wood,color=color.red)
pendulum2 = sphere(radius=0.05,material=materials.wood,color=color.red)

pendulum1.theta = pi/4
pendulum2.theta = pi/2

l = 1
g=9.8
deltat = 0.04

pendulum1.omega = 0
pendulum2.omega = 0

pendulum1.pos = vector(l*sin(pendulum1.theta),1-l*cos(pendulum1.theta),1)
pendulum1.pos = vector(l*sin(pendulum2.theta),1-l*cos(pendulum2.theta),0)

string1 = curve(pos=[support1.pos, pendulum1.pos])
string2 = curve(pos=[support2.pos, pendulum2.pos])

while True:
    rate(1/deltat)
    
    pendulum1.omega -= (g/l)*sin(pendulum1.theta)*deltat
    pendulum2.omega -= (g/l)*sin(pendulum2.theta)*deltat
   
    pendulum1.theta += pendulum1.omega*deltat
    pendulum2.theta += pendulum2.omega*deltat
       
    pendulum1.pos = vector(l*sin(pendulum1.theta),1-l*cos(pendulum1.theta),1)
    pendulum2.pos = vector(l*sin(pendulum2.theta),1-l*cos(pendulum2.theta),0)
    
    string1.pos = [support1.pos, pendulum1.pos]
    string2.pos = [support2.pos, pendulum2.pos]
