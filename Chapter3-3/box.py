from visual import *
from math import *

# build the box
up=box(pos=(0,10.5,0),size=(22,1,20),material=materials.wood)
down=box(pos=(0,-10.5,0),size=(22,1,20),material=materials.wood)
left=box(pos=(10.5,0,0),size=(1,20,20),material=materials.wood)
right=box(pos=(-10.5,0,0),size=(1,20,20),material=materials.wood)
back=box(pos=(0,0,-10.5),size=(22,22,1),material=materials.wood)

# construct balls
b1=sphere(pos=(1,1,0),radius=0.5,material=materials.emissive,make_trail=True,color=color.red)
b2=sphere(pos=(2,2,0),radius=0.5,material=materials.emissive,make_trail=True,color=color.yellow)
b3=sphere(pos=(3,3,0),radius=0.5,material=materials.emissive,make_trail=True,color=color.green)
b4=sphere(pos=(4,4,0),radius=0.5,material=materials.emissive,make_trail=True,color=color.blue)
b5=sphere(pos=(5,5,0),radius=0.5,material=materials.emissive,make_trail=True,color=color.white)

b1.vx,b1.vy,b1.vz=1,sqrt(2),sqrt(3)
b2.vx,b2.vy,b2.vz=sqrt(2),1,sqrt(3)
b3.vx,b3.vy,b3.vz=sqrt(3),sqrt(2),1
b4.vx,b4.vy,b4.vz=sqrt(3),1,sqrt(2)
b5.vx,b5.vy,b5.vz=1,sqrt(3),sqrt(2)

# run

while True:

    rate(1000)

    dt=0.01

    for i in [b1,b2,b3,b4,b5]:
        
        if i.x>10 or i.x<-10:
            i.vx=-i.vx
        if i.y>10 or i.y<-10:
            i.vy=-i.vy
        if i.z>10 or i.z<-10:
            i.vz=-i.vz
        i.x += i.vx*dt
        i.y += i.vy*dt
        i.z += i.vz*dt

    
    


    




