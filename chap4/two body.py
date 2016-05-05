import matplotlib.pyplot as plt
import math


# initial

x1,y1,x2,y2 = [0],[0],[1],[0]
vx1,vy1,vx2,vy2= [0],[-math.pi],[0],[math.pi]
t=[0]
dt=0.002

# run

while t[-1]<10:

    r=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    

    ox1=-4*math.pi*math.pi*(x1[-1]-x2[-1])/(r**3)
    ox2=-4*math.pi*math.pi*(x2[-1]-x1[-1])/(r**3)

    oy1=-4*math.pi*math.pi*(y1[-1]-y2[-1])/(r**3)
    oy2=-4*math.pi*math.pi*(y2[-1]-y1[-1])/(r**3)
    

    vx1.append(vx1[-1]+ox1*dt)
    vx2.append(vx2[-1]+ox2*dt)
    

    vy1.append(vy1[-1]+oy1*dt)
    vy2.append(vy2[-1]+oy2*dt)
    

    x1.append(x1[-1]+vx1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    

    y1.append(y1[-1]+vy1[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    

    t.append(t[-1]+dt)
    
fig=plt.figure(figsize=[8,8])
plt.plot(x1,y1,label='sun')
plt.plot(x2,y2,label='planet')
plt.legend(loc='upper right')

plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('equal mass')


plt.show()
        









    
