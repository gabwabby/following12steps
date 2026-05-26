import numpy
from matplotlib import pyplot as plt
import time,sys

def linearconv(nx):
    dx = 2 / (nx - 1) 
    nt = 20 #number  of timesteps we want to take 
    # dt = 0.025 #delta time, amt of time each timestep covers
    c = 1 #assuming wavespeed of one
    sigma = .5

    dt = sigma * dx

    u = numpy.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

    un = numpy.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * dt/ dx * (un[i] - un[i-1])

    plt.plot(numpy.linspace(0,2,nx), u);
    plt.show()

linearconv(121)

# why it look funny? bc over the time period delta t, the wave is travelling a distane larger than delta x 
# dx of each grid box is related to the # of total points nx so stability can be enforced if the delta t step size is calculated w/r to delta x 

