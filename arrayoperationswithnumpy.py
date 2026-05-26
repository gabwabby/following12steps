import numpy

u = numpy.array((0,1,2,3,4,5))
# for i in range(1, len(u)):
   #print(u[i] - u[i-1])
print(u[1:] - u[0:-1])
