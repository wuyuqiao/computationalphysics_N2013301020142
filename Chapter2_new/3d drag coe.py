from visual import *

# definition of three different drag coefficient
# define drag coefficient of smooth ball
def smooth(x):

    if 0<=x<=150:
        return 0.5
    if 150<=x<=200:
        return -0.008*x+1.7
    if x>200:
        return 0.1

# define drag coefficient of normal ball
def normal(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=150:
        return -0.003*x+0.65
    if x>150:
        return 0.2

# define drag coefficient of rough ball
def rough(x):

    if 0<=x<=50:
        return 0.5
    if 50<=x<=70:
        return -0.02*x+1.5
    if 70<=x<=120:
        return 0.004*x-0.18
    if x>120:
        return 0.3

# initial 
ball1 = sphere(pos=(-30,1,0),radius=0.5,material=materials.wood,make_trail=True,color=color.red)
ball2 = sphere(pos=(-30,1,0),radius=0.5,material=materials.wood,make_trail=True,color=color.green)
ball3 = sphere(pos=(-30,1,0),radius=0.5,material=materials.wood,make_trail=True,color=color.blue)
theta = pi/4
ball1.velo = 50
ball1.velox = ball1.velo*cos(theta)
ball1.veloy = ball1.velo*sin(theta)
ball2.velo = 30.56
ball2.velox = ball2.velo*cos(theta)
ball2.veloy = ball2.velo*sin(theta)
ball3.velo = 30.56
ball3.velox = ball3.velo*cos(theta)
ball3.veloy = ball3.velo*sin(theta)
deltat = 0.01
g = 9.8
text(text='red ball -- smooth \ngreen ball -- normal\nblue ball -- rough',
     align='center', depth=-0.3, color=color.green, pos=(20,20,0),height=3,width=3) 

# move the three balls

while True:

    rate(200)

    # ball1 move
    if ball1.y >= 0:

        co = 1/(3.6**2)
        ball1.velox -= co*smooth(3.6*ball1.velo)*ball1.velo*ball1.velox*deltat
        ball1.veloy -= (g+co*smooth(3.6*ball1.velo)*ball1.velo*ball1.velox)*deltat
        ball1.velo = sqrt((ball1.velox)**2+(ball1.veloy)**2)
        ball1.x += ball1.velox*deltat
        ball1.y += ball1.veloy*deltat

    if ball2.y >= 0:

        co = 1/(3.6**2)
        ball2.velox -= co*normal(3.6*ball2.velo)*ball2.velo*ball2.velox*deltat
        ball2.veloy -= (g+co*smooth(3.6*ball2.velo)*ball2.velo*ball2.velox)*deltat
        ball2.velo = sqrt((ball2.velox)**2+(ball2.veloy)**2)
        ball2.x += ball2.velox*deltat
        ball2.y += ball2.veloy*deltat

    if ball3.y >= 0:

        co = 1/(3.6**2)
        ball3.velox -= co*rough(3.6*ball3.velo)*ball3.velo*ball3.velox*deltat
        ball3.veloy -= (g+co*smooth(3.6*ball3.velo)*ball3.velo*ball3.velox)*deltat
        ball3.velo = sqrt((ball3.velox)**2+(ball3.veloy)**2)
        ball3.x += ball3.velox*deltat
        ball3.y += ball3.veloy*deltat
        
        

        


