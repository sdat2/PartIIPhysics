'''
Core Task 2
by sdat2
Makes a Cornu Spiral graph. Self explanatory?
Ignore Integration warnings.
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import quad

def cosser(x):
	return np.cos(np.pi*(x**2)/2)

def sinner(x):
	return np.sin(np.pi*(x**2)/2)

def Integrator(u):
	C = quad(cosser, 0, u)[0]
	S = quad(sinner, 0, u)[0]
	return C,S

x=[]; y=[]
for i in np.linspace(-2*np.pi,2*np.pi,num=10000):
	C,S = Integrator(i)
	y.append(S); x.append(C)

plt.plot(x,y, color='b', linewidth=1)
plt.plot([0,0], [-0.8,0.8], color= 'r', linewidth=1)
plt.plot([-0.8,0.8], [0,0], color= 'r', linewidth=1)
plt.xlabel('S(u)')
plt.ylabel('C(u)')
plt.xlim([-0.8,0.8])
plt.ylim([-0.8,0.8])

plt.title('The Cornu Spiral')
plt.savefig('C_Cornu_Spiral.pdf')
