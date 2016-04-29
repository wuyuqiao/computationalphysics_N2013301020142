from __future__ import division
from visual import *

bob=sphere(pos=vector(1,0,0),radius=0.01,color=color.red,material=materials.emissive,make_trail=True)
tom=sphere(pos=vector(1.1,0,0),radius=0.01,color=color.green,material=materials.emissive,make_trail=True)
bob.dxdt=0
bob.dydt=0
bob.dzdt=0
bob.t=0
tom.dxdt=0
tom.dydt=0
tom.dzdt=0
tom.t=0
dt=0.001
sigma=10
b=8/3
r=25

while True:
    rate(1000000)
    bob.dxdt=sigma*(bob.y-bob.x)
    bob.dydt=-bob.x*bob.z+r*bob.x-bob.y
    bob.dzdt=bob.x*bob.y-b*bob.z
    bob.x=bob.x+bob.dxdt*dt
    bob.y=bob.y+bob.dydt*dt
    bob.z=bob.z+bob.dzdt*dt
    bob.t=bob.t+dt

    tom.dxdt=sigma*(tom.y-tom.x)
    tom.dydt=-tom.x*tom.z+r*tom.x-tom.y
    tom.dzdt=tom.x*tom.y-b*tom.z
    tom.x=tom.x+tom.dxdt*dt
    tom.y=tom.y+tom.dydt*dt
    tom.z=tom.z+tom.dzdt*dt
    tom.t=tom.t+dt
