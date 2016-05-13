import math
import matplotlib.pyplot as plt

# set the mass of sun, jupiter and earth

gm_sun=4*(math.pi)**2
gm_jupiter=1*gm_sun
gm_earth=gm_sun*(1/330000)

# initialize position and velocity of sun, jupiter and earth

x_earth=[1]
y_earth=[0]
x_sun=[0]
y_sun=[0]
x_jupiter=[5.2]
y_jupiter=[0]

vx_earth=[0]
vy_earth=[2*math.pi]
vx_jupiter=[0]
vy_jupiter=[math.sqrt(gm_sun/5.2)]
vx_sun=[0]
vy_sun=[-math.sqrt(gm_sun/5.2)/1]

# get the trails

dt=0.001
t=[0]

while t[-1]<=100:

    r_es=math.sqrt((x_earth[-1]-x_sun[-1])**2+(y_earth[-1]-y_sun[-1])**2)
    r_ej=math.sqrt((x_earth[-1]-x_jupiter[-1])**2+(y_earth[-1]-y_jupiter[-1])**2)
    r_js=math.sqrt((x_jupiter[-1]-x_sun[-1])**2+(y_jupiter[-1]-y_sun[-1])**2)
    
    vx_earth_new=vx_earth[-1]-gm_sun*(x_earth[-1]-x_sun[-1])*dt/r_es**3-gm_jupiter*(x_earth[-1]-x_jupiter[-1])*dt/r_ej**3
    vy_earth_new=vy_earth[-1]-gm_sun*(y_earth[-1]-y_sun[-1])*dt/r_es**3-gm_jupiter*(y_earth[-1]-y_jupiter[-1])*dt/r_ej**3

    vx_jupiter_new=vx_jupiter[-1]-gm_sun*(x_jupiter[-1]-x_sun[-1])*dt/r_js**3-gm_earth*(x_jupiter[-1]-x_earth[-1])*dt/r_ej**3
    vy_jupiter_new=vy_jupiter[-1]-gm_sun*(y_jupiter[-1]-y_sun[-1])*dt/r_js**3-gm_earth*(y_jupiter[-1]-y_earth[-1])*dt/r_ej**3

    vx_sun_new=vx_sun[-1]-gm_jupiter*(x_sun[-1]-x_jupiter[-1])*dt/r_js**3-gm_earth*(x_sun[-1]-x_earth[-1])*dt/r_es**3
    vy_sun_new=vy_sun[-1]-gm_jupiter*(y_sun[-1]-y_jupiter[-1])*dt/r_js**3-gm_earth*(y_sun[-1]-y_earth[-1])*dt/r_es**3

    vx_earth.append(vx_earth_new)
    vy_earth.append(vy_earth_new)
    vx_jupiter.append(vx_jupiter_new)
    vy_jupiter.append(vy_jupiter_new)
    vx_sun.append(vx_sun_new)
    vy_sun.append(vy_sun_new)

    x_earth.append(x_earth[-1]+vx_earth[-1]*dt)
    y_earth.append(y_earth[-1]+vy_earth[-1]*dt)
    x_jupiter.append(x_jupiter[-1]+vx_jupiter[-1]*dt)
    y_jupiter.append(y_jupiter[-1]+vy_jupiter[-1]*dt)
    x_sun.append(x_sun[-1]+vx_sun[-1]*dt)
    y_sun.append(y_sun[-1]+vy_sun[-1]*dt)

    t.append(t[-1]+dt)

plt.plot(x_earth,y_earth,label='earth')
plt.plot(x_jupiter,y_jupiter,label='jupiter')
plt.plot(x_sun,y_sun,label='sun')

plt.legend(loc='upper right')

plt.title('sun,earth and jupiter, Mass of jupiter=1000Mj')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')

plt.show()



    
    
    
    
