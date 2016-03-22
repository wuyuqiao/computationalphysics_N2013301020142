#Initialize parameters

print 'Please declare the initial situation that we need to continue: '

na_0=float(raw_input('The initial number of A: '))
nb_0=float(raw_input('The initial number of B: '))
t_0=float(raw_input('The initial number of time: '))
dt=float(raw_input('The time step is: '))
na=[na_0]
nb=[nb_0]
t=[t_0]

#Run the calculation

for i in range(200):
    na_next=na[-1]+(nb[-1]-na[-1])*dt
    nb_next=nb[-1]+(na[-1]-nb[-1])*dt
    t_next=t[-1]+dt
    na.append(na_next)
    nb.append(nb_next)
    t.append(t_next)

#Draw the picture
from pylab import *


nana=array(na)
nbnb=array(nb)
tt=array(t)

plot(tt,nana,label='NA',color='b')
plot(tt,nbnb,label='NB',color='r')
grid(True)

yticks([0,10,20,30,40,50,60,70,80,90,100])

legend(loc='upper right',frameon=False)

show()




