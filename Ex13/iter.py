from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Define the G-S function which takes L as argument and returns N_iter

def update_GS(grid,L):

    delta_V = 0

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

def Gauss_Seidel(L):
    
    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <=10:
        grid_impr, delta_V = update_GS(grid_init,L)
        grid_new, delta_V = update_GS(grid_impr,L)
        grid_init = grid_new
        N_iter += 1

    return N_iter

# Define the G-S function which takes L as argument and returns N_iter

def update_GS(grid,L):

    delta_V = 0

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

def Gauss_Seidel(L):
    
    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 5:
        grid_impr, delta_V = update_GS(grid_init,L)
        grid_new, delta_V = update_GS(grid_impr,L)
        grid_init = grid_new
        N_iter += 1

    return N_iter

# Define the SOR function which takes L as argument and returns N_iter

def update_SOR(grid,L):

    delta_V = 0

    for i in range(L):    
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                pass
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                dV = voltage_new - voltage_old
                alpha = 2/(1+(np.pi/L))
                voltage_new = alpha*dV + voltage_old
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

def SOR(L):
    
    grid = []
    for i in range(L):
        row_i = []
        for j in range(L):
            if i==0 or j==0 or i==L-1 or j==L-1:
                voltage = 0
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(70/201)):
                voltage = 1
            elif int(L*(70/201))<=i<=int(L*(130/201)) and j==int(L*(130/201)):
                voltage = -1
            else:
                voltage = 0
            row_i.append(voltage)
        grid.append(row_i)

    epsilon = 10**(-5)*(L-1)**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 5:
        grid_impr, delta_V = update_SOR(grid_init,L)
        grid_new, delta_V = update_SOR(grid_impr,L)
        grid_init = grid_new
        N_iter += 1

    return N_iter
        
l = []
N = []
ll = []
NN = []
for i in range(50):
    l.append(4+i)
    ll.append(4+i)
    N.append(Gauss_Seidel(4+i))
    NN.append(SOR(4+i))

plt.plot(l,N,'yo-',label='Gauss-Seidel')
plt.plot(ll,NN,'r.-',label='SOR')
plt.legend(loc='upper left')
plt.grid(True)
plt.xlabel('L(m)')
plt.ylabel('Number of iteration needed')
plt.title('Number of iteration needed versus L')
plt.show()


    
