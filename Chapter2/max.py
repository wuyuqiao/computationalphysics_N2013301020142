import numpy as np
import math

# define the function which do the calculation with correction

def with_cor(angle):

    # initialize

    x=[0.0]
    y=[0.0]
    vx=[700.0*np.cos(angle)]
    vy=[700.0*np.sin(angle)]
    v=[700.0]
    dt=0.02
    p1=4.0*pow(10.0,-5.0)
    p2=6.5*pow(10.0,-3.0)/280.0
    g=9.8
    alpha=2.5

    # calculate the trajectory

    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] - p1*pow(1-p2*y[-1],alpha)*v[-1]*vx[-1]*dt
        vy_new = vy[-1] - p1*pow(1-p2*y[-1],alpha)*v[-1]*vy[-1]*dt - g*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)

    # determine the land point

    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl

    # result

    return (x,y)


# find the maximum of range and its angle

def find_max(steps):
    angles = list(np.linspace(0,np.pi/2,steps))
    range_=[]
    for i in angles:
        r=with_cor(i)[0][-1]
        range_.append(r)
    max_range=max(range_)
    max_angle=angles[range_.index(max_range)]
    return (max_range,max_angle)

step=[100,150]
error=[100]
while error[0]>=1:
    step[0] += 50
    step[1] += 50
    error[0] = abs(find_max(step[0])[0]-find_max(step[1])[0])

print 'The maximum of range is %f, and the angle is %f' % find_max(step[1])


    
    

