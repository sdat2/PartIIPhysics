import scipy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy.random as rand
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
for i in np.linspace(0,2*np.pi,num=100):
	C,S = Integrator(i)
	y.append(S); x.append(C)

plt.plot(x,y)
plt.xlabel('S(u)')
plt.ylabel('C(u)')
plt.title('The Cornu Spiral')
plt.savefig('C_Cornu_Spiral.pdf')

