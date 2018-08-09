import os
import sys
import scipy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.random

Lower_Bound = 0
Upper_Bound = np.pi/8
Steps = 20 # this is N
Dimensions = 8

def function(coordinate):
	return np.sin(coordinate)

def Monte_Carlo_Integrate(Lower_Bound=0,Upper_Bound=np.pi/8,N=Steps,Dimensions=8):
	estimate = 0
	for i in range(int(N)):
		coordinate= 0
		for j in range(Dimensions): coordinate += float(numpy.random.rand())*(Upper_Bound-Lower_Bound) + Lower_Bound
		estimate += function(coordinate)/N*((Upper_Bound-Lower_Bound)**(Dimensions))
	return estimate*10**6
for i in range(20,1020,20):
	print('for i = ', i, ' ', Monte_Carlo_Integrate(N=i))

Results =[]
for i in range(10,1000,10):
	Results.append(Monte_Carlo_Integrate(N=i))
plt.plot(range(10,1000,10), Results)

c= function(20)
plt.xlabel('Number of Random Numbers')
plt.ylabel('Result')
plt.title('Numerical Integration Test')
plt.savefig('testplot.pdf')
print('for 10^5', Monte_Carlo_Integrate(N=10**5))

plt.clf()
plt.plot(range(10,1000,10),[x-537.1873411 for x in Results],color='black')
u = [537.1873411/x for x in range(10,1000,10)]
l = [-537.1873411/x for x in range(10,1000,10)]
plt.plot(range(10,1000,10),l,color='blue')
plt.plot(range(10,1000,10),u,color='blue')
plt.xlabel('Number of Random Numbers')
plt.ylabel('Result-537.1873411')
plt.savefig('CompareWithReciprocal.pdf')

