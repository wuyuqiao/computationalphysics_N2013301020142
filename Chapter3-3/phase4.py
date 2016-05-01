from numpy import *
import matplotlib.pyplot as plt

def vxx(alpha):
    vtho=sqrt(2)
    vthe=[pi/4]
    vx=[vtho*cos(vthe[-1])]
    vy=[vtho*sin(vthe[-1])]
    x=[1]
    y=[0]
    the=[0]
    t=[0]
    dt=0.01
    xphase=[]
    vxphase=[]
    while t[-1]<50000:
        if -alpha*20<=x[-1]<=alpha*20:
            if y[-1]>20 or y[-1]<-20:
                vy.append(-vy[-1])
                vx.append(vx[-1])
                vthe.append(arctan(float(vy[-1]/vx[-1])))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])

        if x[-1]>alpha*20:
            if y[-1]**2+(x[-1]-alpha*20)**2>=400:
                thee=arctan(float(y[-1]/(x[-1]-alpha*20)))
                vthe.append(pi-vthe[-1]+2*thee)
                vx.append(vtho*cos(vthe[-1]))
                vy.append(vtho*sin(vthe[-1]))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])

        if x[-1]<-alpha*20:
            if y[-1]**2+(x[-1]+alpha*20)**2>=400:
                thee=arctan(float(y[-1]/(x[-1]+alpha*20)))
                vthe.append(pi-vthe[-1]+2*thee)
                vx.append(vtho*cos(vthe[-1]))
                vy.append(vtho*sin(vthe[-1]))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])

        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        the.append(arctan(y[-1]/x[-1]))
        t.append(t[-1]+dt)

        if abs(y[-1])<=0.01:
            xphase.append(x[-1])
            vxphase.append(vx[-1])
            
    return xphase,vxphase



plt.subplot(2,2,1)
x=vxx(0)[0]
vx=vxx(0)[1]
plt.scatter(x,vx,s=0.1)
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0')
plt.ylim(-1.414,1.414)
plt.xlim(-10,10)
plt.grid(True)

plt.subplot(2,2,2)
x=vxx(0.001)[0]
vx=vxx(0.001)[1]
plt.scatter(x,vx,s=0.1)
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0.001')
plt.ylim(-1.414,1.414)
plt.xlim(-10,10)
plt.grid(True)

plt.subplot(2,2,3)
x=vxx(0.01)[0]
vx=vxx(0.01)[1]
plt.scatter(x,vx,s=0.1)
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0.01')
plt.ylim(-1.414,1.414)
plt.xlim(-10,10)
plt.grid(True)

plt.subplot(2,2,4)
x=vxx(0.1)[0]
vx=vxx(0.1)[1]
plt.scatter(x,vx,s=0.1)
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0.1')
plt.ylim(-1.414,1.414)
plt.xlim(-10,10)
plt.grid(True)




plt.show()


            
