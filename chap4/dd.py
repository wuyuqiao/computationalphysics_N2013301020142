import matplotlib.pyplot as plt
import math

# this function gives trac
def trac(vxx,vyy):
    x=[1]
    y=[0]   
    vx=[vxx]
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

x1=trac(math.sqrt(2)*math.pi,math.sqrt(2)*math.pi)[0]
y1=trac(math.sqrt(2)*math.pi,math.sqrt(2)*math.pi)[1]
x2=trac(0,2*math.pi)[0]
y2=trac(0,2*math.pi)[1]
x3=trac(-math.sqrt(2)*math.pi,math.sqrt(2)*math.pi)[0]
y3=trac(-math.sqrt(2)*math.pi,math.sqrt(2)*math.pi)[1]

plt.plot(x1,y1,label='theta=45')
plt.plot(x2,y2,label='theta=90')
plt.plot(x3,y3,label='theta=135')
plt.scatter([0],[0],s=1000,color='yellow')
plt.legend(loc='upper right')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('trajectory for different initial velocity')

plt.show()
        
        
