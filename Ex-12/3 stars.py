import math
import matplotlib.pyplot as plt

# set the mass of three suns 

gm=4*(math.pi)**2


# initialize position and velocity of sun, jupiter and earth

x1=[0]
y1=[5/math.sqrt(3)]
x2=[5/2]
y2=[-5/(2*math.sqrt(3))]
x3=[-5/2]
y3=[-5/(2*math.sqrt(3))]
xe=[0]
ye=[0]

vx1=[0.7*2*math.sqrt(15)*math.pi/5]
vy1=[0]
vx2=[-0.7*math.sqrt(15)*math.pi/5]
vy2=[-0.7*3*math.sqrt(5)*math.pi/5]
vx3=[-0.7*math.sqrt(15)*math.pi/5]
vy3=[0.7*3*math.sqrt(5)*math.pi/5]

vxe=[0]
vye=[0]

# get the trails

dt=0.00001
t=[0]

while t[-1]<=20:

    r12=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    r23=math.sqrt((x2[-1]-x3[-1])**2+(y2[-1]-y3[-1])**2)
    r13=math.sqrt((x1[-1]-x3[-1])**2+(y1[-1]-y3[-1])**2)

    r1=math.sqrt((xe[-1]-x1[-1])**2+(ye[-1]-y1[-1])**2)
    r2=math.sqrt((xe[-1]-x2[-1])**2+(ye[-1]-y2[-1])**2)
    r3=math.sqrt((xe[-1]-x3[-1])**2+(ye[-1]-y3[-1])**2)

    vx1_new=vx1[-1]-gm*(x1[-1]-x2[-1])*dt/r12**3-gm*(x1[-1]-x3[-1])*dt/r13**3
    vx2_new=vx2[-1]-gm*(x2[-1]-x1[-1])*dt/r12**3-gm*(x2[-1]-x3[-1])*dt/r23**3
    vx3_new=vx3[-1]-gm*(x3[-1]-x1[-1])*dt/r13**3-gm*(x3[-1]-x2[-1])*dt/r23**3

    vy1_new=vy1[-1]-gm*(y1[-1]-y2[-1])*dt/r12**3-gm*(y1[-1]-y3[-1])*dt/r13**3
    vy2_new=vy2[-1]-gm*(y2[-1]-y1[-1])*dt/r12**3-gm*(y2[-1]-y3[-1])*dt/r23**3
    vy3_new=vy3[-1]-gm*(y3[-1]-y1[-1])*dt/r13**3-gm*(y3[-1]-y2[-1])*dt/r23**3

    vxe_new=vxe[-1]-gm*(xe[-1]-x1[-1])*dt/r1**3-gm*(xe[-1]-x2[-1])*dt/r2**3-gm*(xe[-1]-x3[-1])*dt/r3**3
    vye_new=vye[-1]-gm*(ye[-1]-y1[-1])*dt/r1**3-gm*(ye[-1]-y2[-1])*dt/r2**3-gm*(ye[-1]-y3[-1])*dt/r3**3

    vx1.append(vx1_new)
    vx2.append(vx2_new)
    vx3.append(vx3_new)

    vy1.append(vy1_new)
    vy2.append(vy2_new)
    vy3.append(vy3_new)

    vxe.append(vxe_new)
    vye.append(vye_new)

    x1.append(x1[-1]+vx1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    x3.append(x3[-1]+vx3[-1]*dt)

    y1.append(y1[-1]+vy1[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    y3.append(y3[-1]+vy3[-1]*dt)

    xe.append(xe[-1]+vxe[-1]*dt)
    ye.append(ye[-1]+vye[-1]*dt)    

    t.append(t[-1]+dt)


plt.plot(xe,ye)



plt.title('3 suns and earth, earth only')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')


plt.show()



    
    
    
    
