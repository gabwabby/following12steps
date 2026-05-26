import numpy
from matplotlib import pyplot as plt
import time,sys

nx = 41
dx = 2 / (nx - 1) 
nt = 25 #number  of timesteps we want to take 
dt = 0.025 #delta time, amt of time each timestep covers
c = 1 #assuming wavespeed of one

u = numpy.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)

plt.plot(numpy.linspace(0,2,nx), u);
plt.show()


un = numpy.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - c * dt/ dx * (un[i] - un[i-1])


plt.plot(numpy.linspace(0,2,nx), u);
plt.show()

# why is it moving to the right? 