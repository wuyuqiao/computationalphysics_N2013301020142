from visual import *
from math import *

shape=Polygon([(-0.5,-0.5),(-0.5,0.5),(0.5,0.5),(0.5,-0.5)])
path=paths.arc(radius=20.5,angle2=2*pi)
tableup=extrusion(pos=path,shape=shape,material=materials.wood,color=color.green)
tabledo=cylinder(pos=(0,-1,0),axis=(0,1,0),material=materials.wood,radius=20)
taiqiu=sphere(pos=(2,0.5,0),radius=0.5,color=color.yellow,make_trail=True,material=materials.emissive)
taiqiu.tho=1
taiqiu.the=0
taiqiu.vtho=sqrt(2)
taiqiu.vthe=pi/4
taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)
dt=0.01
while True:
    rate(10000)

    if taiqiu.x**2+taiqiu.z**2>400:
        taiqiu.vthe=pi-taiqiu.vthe+2*taiqiu.the

    taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
    taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)
    
    taiqiu.x=taiqiu.x+taiqiu.vx*dt
    taiqiu.z=taiqiu.z+taiqiu.vz*dt
    taiqiu.tho=sqrt(taiqiu.x**2+taiqiu.z**2)
    taiqiu.the=arctan(float(taiqiu.z/taiqiu.x))
    
    
    
