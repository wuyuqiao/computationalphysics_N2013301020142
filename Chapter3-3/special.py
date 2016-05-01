from visual import *

shape=Polygon([(-0.5,-0.5),(-0.5,0.5),(0.5,0.5),(0.5,-0.5)])
path1=paths.arc(radius=4.5,angle2=2*pi)
path2=[(10.5,0,10.5),(10.5,0,-10.5),(-10.5,0,-10.5),(-10.5,0,10.5),(10.5,0,10.5)]
table1=extrusion(pos=path1,shape=shape,material=materials.wood,color=color.red)
table2=extrusion(pos=path2,shape=shape,material=materials.wood,color=color.green)
table3=box(pos=(0,-1,0),size=(20,1,20),material=materials.wood)

taiqiu=sphere(pos=(7.5,0.5,0),radius=0.1,color=color.yellow,make_trail=True,material=materials.emissive)
taiqiu.tho=1
taiqiu.the=0
taiqiu.vtho=1
taiqiu.vthe=pi/12
taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)
dt=0.001

while True:
    rate(10000)

    if taiqiu.x**2+taiqiu.z**2<=25:
        taiqiu.vthe=pi-taiqiu.vthe+2*taiqiu.the
        while taiqiu.vthe>=2*pi:
            taiqiu.vthe-=2*pi
        while taiqiu.vthe<=0:
            taiqiu.vthe+=2*pi
        taiqiu.vx=taiqiu.vtho*cos(taiqiu.vthe)
        taiqiu.vz=taiqiu.vtho*sin(taiqiu.vthe)

    if taiqiu.x>=10:
        taiqiu.vx=-taiqiu.vx
        taiqiu.vthe=pi
    if taiqiu.x<=-10:
        taiqiu.vx=-taiqiu.vx
        taiqiu.vthe=0
    if taiqiu.z>=10:
        taiqiu.vz=-taiqiu.vz
        taiqiu.vthe=3*pi/2
    if taiqiu.z<=-10:
        taiqiu.vz=-taiqiu.vz
        taiqiu.vthe=pi/2

    taiqiu.x=taiqiu.x+taiqiu.vx*dt
    taiqiu.z=taiqiu.z+taiqiu.vz*dt
    taiqiu.tho=sqrt(taiqiu.x**2+taiqiu.z**2)
    taiqiu.the=arctan(float(taiqiu.z/taiqiu.x))
        
        

