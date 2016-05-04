from visual import *

def get_v(radius,period):
    return vector(0,2*pi*radius/period,0)

mercury = sphere(pos=(0.39,0,0),color=color.blue,radius=0.06,make_trail=True)
venus   = sphere(pos=(0.72,0,0),color=color.yellow,radius=0.06,make_trail=True)
earth   = sphere(pos=(1,0,0),material=materials.earth,radius=0.06,make_trail=True)
mars    = sphere(pos=(1.52,0,0),color=color.red,radius=0.06,make_trail=True)
sun     = sphere(pos=(0,0,0),color=color.orange,material=materials.emissive,radius=0.2,make_trail=True)

mercury.velo=get_v(0.39,0.241)
venus.velo=get_v(0.72,0.615)
earth.velo=get_v(1,1)
mars.velo=get_v(1.52,1.88)
dt=0.002

while True:
    rate(200)
    for p in [mercury,venus,earth,mars]:
        r=sqrt((p.x)**2+(p.y)**2)
        p.velo = p.velo-vector(4*(pi**2)*p.x*dt/(r**3),4*(pi**2)*p.y*dt/(r**3),0)
        p.pos  = p.pos+(p.velo[0]*dt,p.velo[1]*dt,0)


