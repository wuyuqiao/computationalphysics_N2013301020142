from __future__ import division
from visual import *
from math import *

# add some constants
q=0.5
l=9.8
g=9.8
f=2/3
dt=0.04
theta01=0.2
theta02=0.21
omega0=0

# add three ceilings
ceil1=box(pos=(-20,5,0),size=(5,0.5,2),material=materials.bricks)
ceil2=box(pos=(0,5,0),size=(5,0.5,2),material=materials.bricks)


ball1=sphere(pos=(-20+l*sin(theta01),5-l*cos(theta01),0),radius=1,material=materials.emissive,color=color.red)
ball2=sphere(pos=(l*sin(theta02),5-l*cos(theta02),0),radius=1,material=materials.emissive,color=color.yellow)
ball3=sphere(pos=(20,0,0),radius=1,material=materials.wood)
ball4=sphere(pos=(30,0,0),radius=1,material=materials.emissive,color=color.green)

ball1.omega=omega0
ball2.omega=omega0


ball1.theta=theta01
ball2.theta=theta02


ball1.t=0
ball2.t=0


ball1.F=1.2
ball2.F=1.2


string1=curve(pos=[ceil1.pos,ball1.pos],color=color.red)
string2=curve(pos=[ceil2.pos,ball2.pos],color=color.yellow)
string3=curve(pos=[ball3.pos,ball4.pos],color=color.green)

po1=arrow(pos=ball1.pos,axis=(10*ball1.omega*cos(ball1.theta),10*ball1.omega*sin(ball1.theta),0),color=color.red)
po2=arrow(pos=ball2.pos,axis=(10*ball2.omega*cos(ball2.theta),10*ball2.omega*sin(ball2.theta),0),color=color.yellow)

while True:

    rate(100)

    ball1.omega=ball1.omega-((g/l)*sin(ball1.theta)+q*ball1.omega-ball1.F*sin(f*ball1.t))*dt
    ball2.omega=ball2.omega-((g/l)*sin(ball2.theta)+q*ball2.omega-ball2.F*sin(f*ball2.t))*dt
    

    angle1_new=ball1.theta+ball1.omega*dt
    while angle1_new>pi:
        angle1_new-=2*pi
    while angle1_new<-pi:
        angle1_new+=2*pi

    angle2_new=ball2.theta+ball2.omega*dt
    while angle2_new>pi:
        angle2_new-=2*pi
    while angle2_new<-pi:
        angle2_new+=2*pi


    ball1.theta=angle1_new
    ball2.theta=angle2_new
    

    ball1.pos=(-20+l*sin(ball1.theta),5-l*cos(ball1.theta),0)
    ball2.pos=(l*sin(ball2.theta),5-l*cos(ball2.theta),0)
    det=abs(ball1.theta-ball2.theta)
    ball4.pos=(20+10*cos(det),10*sin(det),0)
    

    string1.pos=[ceil1.pos,ball1.pos]
    string2.pos=[ceil2.pos,ball2.pos]
    string3.pos=[ball3.pos,ball4.pos]

    po1.pos=ball1.pos
    po2.pos=ball2.pos
    

    po1.axis=(10*ball1.omega*cos(ball1.theta),10*ball1.omega*sin(ball1.theta),0)
    po2.axis=(10*ball2.omega*cos(ball2.theta),10*ball2.omega*sin(ball2.theta),0)
    
    ball1.t=ball1.t+dt
    ball2.t=ball2.t+dt
    
