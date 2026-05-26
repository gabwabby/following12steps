import numpy
from matplotlib import pyplot

myarray = numpy.linspace(0, 5, 10)
# print(myarray)

# linspace works like
# h = (stop - start) / (num - 1) 
# h = (5 - 0) / (10 - 1)

# for i in range(5): 
    # print("Hi \n") # \n line break

#for i in range(3):
    #for j in range(3):
        #print(i,j)
    #print("This statement is within the i-loop, but not the j-loop")

myvals = numpy.array([1, 2, 3, 4, 5])
# print(myvals[0:2]) #inclusive on the front end and exclusive on the back so yes 1, no 3

a = numpy.linspace(1,5,5)
b = a
a[2] = 17
c = a.copy() # now c has its own sep memory so if i were to edit a, it wont change whats in c 
a[2] = 3
print(a) 
print(b)
print(c)
