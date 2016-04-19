from visual import *

# define drag coefficient of normal ball
def normal(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=150:
        return -0.003*x+0.65
    if x>150:
        return 0.2

# define five balls

ball1=sphere(pos=(-10,1,0),radius=0.2,material=materials.marble,color=color.red,make_trail=True)
ball2=sphere(pos=(-10,1,0),radius=0.2,material=materials.marble,color=color.orange,make_trail=True)
ball3=sphere(pos=(-10,1,0),radius=0.2,material=materials.marble,color=color.yellow,make_trail=True)
ball4=sphere(pos=(-10,1,0),radius=0.2,material=materials.marble,color=color.green,make_trail=True)
ball5=sphere(pos=(-10,1,0),radius=0.2,material=materials.marble,color=color.blue,make_trail=True)
box(pos=(0,-2,0),size=(200,4,100),material=materials.wood)

# define constants

theta = pi/4
g=9.8
S=0.00041
deltat=0.001

# initial the balls' location and velocity (3 dimensions)

ball1.velo=100
ball2.velo=100
ball3.velo=100
ball4.velo=100
ball5.velo=100

ball1.velox=100*cos(theta)
ball2.velox=100*cos(theta)
ball3.velox=100*cos(theta)
ball4.velox=100*cos(theta)
ball5.velox=100*cos(theta)

ball1.veloy=100*sin(theta)
ball2.veloy=100*sin(theta)
ball3.veloy=100*sin(theta)
ball4.veloy=100*sin(theta)
ball5.veloy=100*sin(theta)

ball1.veloz=0
ball2.veloz=0
ball3.veloz=0
ball4.veloz=0
ball5.veloz=0

ball1.omegax=0
ball2.omegax=0
ball3.omegax=0
ball4.omegax=0
ball5.omegax=0

ball1.omegay=0
ball2.omegay=100
ball3.omegay=500
ball4.omegay=1000
ball5.omegay=2000

ball1.omegaz=0
ball2.omegaz=0
ball3.omegaz=0
ball4.omegaz=0
ball5.omegaz=0

# update balls

while True:

    rate(700)

    #update ball1

    if ball1.y >= 0:
        
        co = 1/(3.6**2)

        ball1.velox += -co*normal(3.6*ball1.velo)*ball1.velo*ball1.velox*deltat + 0.00041*(ball1.omegay*ball1.veloz-ball1.omegaz*ball1.veloy)*deltat
        ball1.veloy += -co*normal(3.6*ball1.velo)*ball1.velo*ball1.veloy*deltat + 0.00041*(ball1.omegaz*ball1.velox-ball1.omegax*ball1.veloz)*deltat - g*deltat
        ball1.veloz += -co*normal(3.6*ball1.velo)*ball1.velo*ball1.veloz*deltat + 0.00041*(ball1.omegax*ball1.veloy-ball1.omegay*ball1.velox)*deltat
        ball1.velo = sqrt((ball1.velox)**2+(ball1.veloy)**2+(ball1.veloz)**2)

        ball1.x += ball1.velox*deltat
        ball1.y += ball1.veloy*deltat
        ball1.z += ball1.veloz*deltat

    # update ball2

    if ball2.y >= 0:

        co = 1/(3.6**2)

        ball2.velox += -co*normal(3.6*ball2.velo)*ball2.velo*ball2.velox*deltat + 0.00041*(ball2.omegay*ball2.veloz-ball2.omegaz*ball2.veloy)*deltat
        ball2.veloy += -co*normal(3.6*ball2.velo)*ball2.velo*ball2.veloy*deltat + 0.00041*(ball2.omegaz*ball2.velox-ball2.omegax*ball2.veloz)*deltat - g*deltat
        ball2.veloz += -co*normal(3.6*ball2.velo)*ball2.velo*ball2.veloz*deltat + 0.00041*(ball2.omegax*ball2.veloy-ball2.omegay*ball2.velox)*deltat
        ball2.velo = sqrt((ball2.velox)**2+(ball2.veloy)**2+(ball2.veloz)**2)

        ball2.x += ball2.velox*deltat
        ball2.y += ball2.veloy*deltat
        ball2.z += ball2.veloz*deltat

    # update ball3

    if ball3.y >= 0:

        co = 1/(3.6**2)

        ball3.velox += -co*normal(3.6*ball3.velo)*ball3.velo*ball3.velox*deltat + 0.00041*(ball3.omegay*ball3.veloz-ball3.omegaz*ball3.veloy)*deltat
        ball3.veloy += -co*normal(3.6*ball3.velo)*ball3.velo*ball3.veloy*deltat + 0.00041*(ball3.omegaz*ball3.velox-ball3.omegax*ball3.veloz)*deltat - g*deltat
        ball3.veloz += -co*normal(3.6*ball3.velo)*ball3.velo*ball3.veloz*deltat + 0.00041*(ball3.omegax*ball3.veloy-ball3.omegay*ball3.velox)*deltat
        ball3.velo = sqrt((ball3.velox)**2+(ball3.veloy)**2+(ball3.veloz)**2)

        ball3.x += ball3.velox*deltat
        ball3.y += ball3.veloy*deltat
        ball3.z += ball3.veloz*deltat

    # update ball4

    if ball4.y >= 0:

        co = 1/(3.6**2)

        ball4.velox += -co*normal(3.6*ball4.velo)*ball4.velo*ball4.velox*deltat + 0.00041*(ball4.omegay*ball4.veloz-ball4.omegaz*ball4.veloy)*deltat
        ball4.veloy += -co*normal(3.6*ball4.velo)*ball4.velo*ball4.veloy*deltat + 0.00041*(ball4.omegaz*ball4.velox-ball4.omegax*ball4.veloz)*deltat - g*deltat
        ball4.veloz += -co*normal(3.6*ball4.velo)*ball4.velo*ball4.veloz*deltat + 0.00041*(ball4.omegax*ball4.veloy-ball4.omegay*ball4.velox)*deltat
        ball4.velo = sqrt((ball4.velox)**2+(ball4.veloy)**2+(ball4.veloz)**2)

        ball4.x += ball4.velox*deltat
        ball4.y += ball4.veloy*deltat
        ball4.z += ball4.veloz*deltat

    # update ball5

    if ball5.y >= 0:

        co = 1/(3.6**2)

        ball5.velox += -co*normal(3.6*ball5.velo)*ball5.velo*ball5.velox*deltat + 0.00041*(ball5.omegay*ball5.veloz-ball5.omegaz*ball5.veloy)*deltat
        ball5.veloy += -co*normal(3.6*ball5.velo)*ball5.velo*ball5.veloy*deltat + 0.00041*(ball5.omegaz*ball5.velox-ball5.omegax*ball5.veloz)*deltat - g*deltat
        ball5.veloz += -co*normal(3.6*ball5.velo)*ball5.velo*ball5.veloz*deltat + 0.00041*(ball5.omegax*ball5.veloy-ball5.omegay*ball5.velox)*deltat
        ball5.velo = sqrt((ball5.velox)**2+(ball5.veloy)**2+(ball5.veloz)**2)

        ball5.x += ball5.velox*deltat
        ball5.y += ball5.veloy*deltat
        ball5.z += ball5.veloz*deltat

    
            
        
    

