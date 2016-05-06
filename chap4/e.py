import matplotlib.pyplot as plt
import math
import numpy as np

# this function gives trac
def velo(e):
    a=0.39
    x=[0.47]
    y=[0]   
    vx=[0]
    vy0=2*math.pi*math.sqrt((1-e)/0.47)
    vy=[vy0]
    t=[0]
    dt=0.0001
    rr=[0.47]
    angle=[0]
    the=[0]
    tmax=[0]
    
    while t[-1]<20:
        alpha=0.000000011

        r2=x[-1]**2+y[-1]**2
        r=math.sqrt(r2)

        ox=-4*math.pi*math.pi*(x[-1])/(r**3)-4*alpha*math.pi*math.pi*(x[-1])/(r**5)
        oy=-4*math.pi*math.pi*(y[-1])/(r**3)-4*alpha*math.pi*math.pi*(y[-1])/(r**5)

        vx.append(vx[-1]+ox*dt)
        vy.append(vy[-1]+oy*dt)

        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)

        if x>=0 and y>=0:
            theta=np.arctan(y[-1]/x[-1])
        if x<=0 and y>=0:
            theta=math.pi+np.arctan(y[-1]/x[-1])
        if x<=0 and y<=0:
            theta=math.pi+np.arctan(y[-1]/x[-1])
        if x>=0 and y<=0:
            theta=2*math.pi+np.arctan(y[-1]/x[-1])

        angle.append(theta)            
        rr.append(r)
        t.append(t[-1]+dt)

    for i in range(len(rr)):
        if i!=0 and i!=len(rr)-1 and rr[i]>rr[i-1] and rr[i]>rr[i+1]:
            the.append(angle[i])
            tmax.append(t[i])
    

    velo=float((the[1]-the[0])/(tmax[1]-tmax[0]))        
    return velo

x=list(np.linspace(0.05,0.95,400))
y=[]
for i in x:
    y.append(360*180*velo(i)/math.pi)

plt.plot(x,y)
plt.xlim(0.05,0.95)
plt.title('precession velocity versus eccentricities')
plt.xlabel('eccentricity')
plt.ylabel('precession velocity(arc/yr)')
plt.show()
