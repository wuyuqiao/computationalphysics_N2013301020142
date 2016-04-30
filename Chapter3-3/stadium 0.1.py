from visual import *
from math import *

# background
alpha=0.1
shape=Polygon([(-0.5,-0.5),(-0.5,0.5),(0.5,0.5),(0.5,-0.5)])
path=[]
for i in range(181):
    newx=20*cos(i*pi/180)
    newz=alpha*20+20*sin(i*pi/180)
    path.append((newx,0,newz))

for j in range(181):
    newx=20*cos(pi+(j*pi)/180)
    newz=-alpha*20-20*sin(j*pi/180)
    path.append((newx,0,newz))
path.append((20,0,alpha*20))
bob=box(pos=(0,-1,0),size=(40,1,45),material=materials.wood)
tableup=extrusion(pos=path,shape=shape,material=materials.wood,color=color.green)

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

    if -alpha*20<=taiqiu.z<=alpha*20:
        if taiqiu.x>20 or taiqiu.x<-20:
            taiqiu.vx=-taiqiu.vx
            taiqiu.vthe=arctan(float(taiqiu.vz/taiqiu.vx))
    if taiqiu.z>alpha*20:
        if taiqiu.x**2+(taiqiu.z-alpha*20)**2>400:
            the=arctan(float((taiqiu.z-alpha*20)/taiqiu.x))
            taiqiu.vthe=pi-taiqiu.vthe+2*the
            taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
            taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)
    if taiqiu.z<-alpha*20:
        if taiqiu.x**2+(taiqiu.z+alpha*20)**2>400:
            the=arctan(float((taiqiu.z+alpha*20)/taiqiu.x))
            taiqiu.vthe=pi-taiqiu.vthe+2*the
            taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
            taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)
    
    taiqiu.x=taiqiu.x+taiqiu.vx*dt
    taiqiu.z=taiqiu.z+taiqiu.vz*dt
    taiqiu.tho=sqrt(taiqiu.x**2+taiqiu.z**2)
    taiqiu.the=arctan(float(taiqiu.z/taiqiu.x))
