from __future__ import division
import numpy as np
from copy import deepcopy
from cmath import *
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)

y_now = np.exp(-1000*(x-0.5)**2) 
y_now[0] = 0
y_now[-1] = 0

y_before = deepcopy(y_now)
y_after = np.zeros(101)
disp = [y_now[5]]
t = [0]

for j in range(2**(10)-1):

    for i in range(101):
        if i== 0 or i== 100:
            y_after[i] = 0
        else:
            y_after[i] = - y_before[i] + y_now[i+1] + y_now[i-1]

    y_before = deepcopy(y_now)
    y_now = deepcopy(y_after)
    disp.append(y_now[5])
    t.append((j+1)*10**(-4)/3)

disp_fft = np.fft.fft(disp)
disp_power = []
frequency = []
for i in range(1024):
    if i==0:
        disp_power.append(abs(disp_fft[i]))
        f = 0
        frequency.append(f)
    else:
        disp_power.append(abs(disp_fft[i]))
        T = 1024*10**(-4)/(3*i)
        f = 1/T
        frequency.append(f)

plt.plot(frequency, disp_power)

plt.xlabel('Frequency(Hz)')
plt.ylabel('Power(arbitrary units)')
plt.title('Power spectrum')
plt.xlim(0,3000)

plt.show()

        
    
    
