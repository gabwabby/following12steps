from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

nx = 81
ny = 81
nt = 100 
c = 1 
dx = 2 / (nx - 1) 
dy = 2 / (ny - 1) 
sigma = 0.2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx))
un = numpy.ones((ny, nx))

##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 

#fig = plt.figure(figsize=(11, 7), dpi=100)
#ax = fig.add_subplot(projection='3d')                      
#X, Y = numpy.meshgrid(x, y)                            
#surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
#plt.show()

#check above against step5 image

for n in range(nt + 1): 
    un = u.copy() 
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j,i] = (un[j,i] + ( c * dt / dx * (un[j, i] - un[j, i-1])) - ( c * dt / dy * (un[j, i] - un[j - 1, i])))
            u[0,:] = 1
            u[-1,:] = 1
            u[:,0] = 1
            u[:,-1] = 1

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')
X, Y = numpy.meshgrid(x, y)   
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()

# this is wrong bro