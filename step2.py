import numpy
from matplotlib import pyplot as plt
import time,sys

nx = 41
dx = 2 / (nx - 1) 
nt = 20 #number  of timesteps we want to take 
dt = 0.025 #delta time, amt of time each timestep covers
c = 1 #assuming wavespeed of one

u = numpy.ones(nx)
u[int(.5 /dx): int(1 / dx + 1)] = 2 

un = numpy.ones(nx) 

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])


plt.plot(numpy.linspace(0,2,nx), u);
plt.show()

# What do you observe about the evolution of the hat function under the nonlinear convection equation? What happens when you change the numerical parameters and run again?
