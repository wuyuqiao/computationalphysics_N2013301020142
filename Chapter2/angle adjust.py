import numpy as np
import math

# define a function which takes the y, velocity, wind, and angle as input, then give you the x

def get_x(y0,velo,angle,vwind):

    # initialize

    x=[0.0]
    y=[0.0]
    vx=[float(velo)*float(np.cos(angle))]
    vy=[float(velo)*float(np.sin(angle))]
    v=[float(velo)]
    dt=0.02
    p1=4.0*pow(10.0,-5.0)
    p2=6.5*pow(10.0,-3.0)/280.0
    g=9.8
    alpha=2.5

    # calculate the trajectory

    while y[-1]>=y0 or vy[-1]>=0 :
        x_new = x[-1] + (vx[-1] + vwind)*dt
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

    r = float((y[-2]-y0)/(y0-y[-1]))
    xl = (x[-2]+r*x[-1])/(r+1)
    yl = y0
    x[-1] = xl
    y[-1] = yl

    # result

    return x[-1]

# find the maximum of range and its angle

def find_max(steps,y0,velo,vwind):
    angles = list(np.linspace(0,np.pi/2,steps))
    range_=[]
    for i in angles:
        r=get_x(y0,velo,i,vwind)
        range_.append(r)
    max_range=max(range_)
    max_angle=angles[range_.index(max_range)]
    return (max_range,max_angle)

# define a function which takes the coordinates of target, velocity, wind, accuracy as input, and give you the angle

def angl(x,y,velo,vwind,accu):

    s=int(30000.0/accu)
    mr=find_max(s,y,velo,vwind)[0]
    ma=find_max(s,y,velo,vwind)[1]

    if x>mr:
        print 'Sorry, the shell cannot go that far'
    elif x==mr:
        return ma,mr
    else:
        angle_1 = ma
        angle_2 = ma
        
        while get_x(y,velo,angle_1,vwind) > (x + 10*accu/2.0):
            angle_1 -= 0.0001
        while get_x(y,velo,angle_2,vwind) > (x + 10*accu/2.0):
            angle_2 += 0.0001
        while get_x(y,velo,angle_1,vwind) > (x + accu/2.0):
            angle_1 -= 0.00001
        while get_x(y,velo,angle_2,vwind) > (x + accu/2.0):
            angle_2 += 0.00001
        
        return ((angle_1,get_x(y,velo,angle_1,vwind)),(angle_2,get_x(y,velo,angle_2,vwind)))
    




    
    

    
        
    
    
    
    
    
