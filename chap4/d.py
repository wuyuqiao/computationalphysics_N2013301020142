import matplotlib.pyplot as plt
import math

# this function gives trac
def trac(vyy):
    x=[1]
    y=[0]   
    vx=[0]
    vy=[vyy]
    t=[0]
    dt=0.002

    while t[-1]<=4:
        r2=(x[-1])**2+(y[-1])**2
        r=math.sqrt(r2)
        ox=-4*math.pi*math.pi*x[-1]/(r**3)
        oy=-4*math.pi*math.pi*y[-1]/(r**3)
        vx.append(vx[-1]+ox*dt)
        vy.append(vy[-1]+oy*dt)
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        t.append(t[-1]+dt)

    return x,y

fig=plt.figure(figsize=[8,8])
x1=trac(2*math.pi)[0]
y1=trac(2*math.pi)[1]
x2=trac(2.1*math.pi)[0]
y2=trac(2.1*math.pi)[1]
x3=trac(1.5*math.pi)[0]
y3=trac(1.5*math.pi)[1]
plt.plot(x1,y1,label='vy0=2pi')
plt.plot(x2,y2,label='vy0=2.1pi')
plt.plot(x3,y3,label='vy0=1.5pi')
plt.scatter([0],[0],s=1000,color='yellow')
plt.legend(loc='upper right')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('trajectory for different initial velocity')

plt.show()
        
        
