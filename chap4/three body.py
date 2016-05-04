import matplotlib.pyplot as plt
import math
from random import *

# initial

x1,y1,x2,y2,x3,y3 = [-5],[20],[10],[3.3],[-14],[-3]
vx1,vy1,vx2,vy2,vx3,vy3 = [-math.sqrt(2)],[0],[math.sqrt(2)/2],[0],[math.sqrt(2)/2],[0]
t=[0]
dt=0.002

# run

while t[-1]<50:

    r12=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    r13=math.sqrt((x1[-1]-x3[-1])**2+(y1[-1]-y3[-1])**2)
    r23=math.sqrt((x2[-1]-x3[-1])**2+(y2[-1]-y3[-1])**2)

    ox1=-4*math.pi*math.pi*(x1[-1]-x2[-1])/(r12**3)-4*math.pi*math.pi*(x1[-1]-x3[-1])/(r13**3)
    ox2=-4*math.pi*math.pi*(x2[-1]-x1[-1])/(r12**3)-4*math.pi*math.pi*(x2[-1]-x3[-1])/(r23**3)
    ox3=-4*math.pi*math.pi*(x3[-1]-x1[-1])/(r13**3)-4*math.pi*math.pi*(x3[-1]-x2[-1])/(r23**3)

    oy1=-4*math.pi*math.pi*(y1[-1]-y2[-1])/(r12**3)-4*math.pi*math.pi*(y1[-1]-y3[-1])/(r13**3)
    oy2=-4*math.pi*math.pi*(y2[-1]-y1[-1])/(r12**3)-4*math.pi*math.pi*(y2[-1]-y3[-1])/(r23**3)
    oy3=-4*math.pi*math.pi*(y3[-1]-y1[-1])/(r13**3)-4*math.pi*math.pi*(y3[-1]-y2[-1])/(r23**3)

    vx1.append(vx1[-1]+ox1*dt)
    vx2.append(vx2[-1]+ox2*dt)
    vx3.append(vx3[-1]+ox3*dt)

    vy1.append(vy1[-1]+oy1*dt)
    vy2.append(vy2[-1]+oy2*dt)
    vy3.append(vy3[-1]+oy3*dt)

    x1.append(x1[-1]+vx1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    x3.append(x3[-1]+vx3[-1]*dt)

    y1.append(y1[-1]+vy1[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    y3.append(y3[-1]+vy3[-1]*dt)

    t.append(t[-1]+dt)
    
fig=plt.figure(figsize=[8,8])
plt.plot(x1,y1,label='sun 1')
plt.plot(x2,y2,label='sun 2')
plt.plot(x3,y3,label='sun 3')
plt.scatter([x1[-1],x2[-1],x3[-1]],[y1[-1],y2[-1],y3[-1]],color="black",s=50)
plt.scatter([x1[0],x2[0],x3[0]],[y1[0],y2[0],y3[0]],color="red",s=50)
plt.legend(loc='upper right')

plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('three body problem')


plt.show()
        









    
