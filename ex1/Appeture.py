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
	C = quad(cosser,0,u)[0]
	S = quad(sinner,0,u)[0]
	return C,S

x=[]; y=[]

def Two_Ended(x0,x1,lam=0.01,D=0.3):
	Scaling = (2/(lam*D))**0.5
	u2 = x1*Scaling; u1 = x0*Scaling
	imag1,real1 = Integrator(u1)
	imag2,real2 = Integrator(u2)
	imag = -imag1+imag2
	real = -real1+real2
	mag = (imag**2+real**2)*0.5
	arg = np.arctan(imag/real)
	return mag, arg


def Plot_Mag_Arg(d=0.1,lam = 0.01,D=0.3):
	mag_list = []; arg_list =[]
	x = np.linspace(-0.8,0.8,num=1000)
	for i in x:
		mag, arg = Two_Ended(i,i+d,D=D,lam=lam)
		mag_list.append(mag); arg_list.append(arg)
	plt.plot(x,mag_list)
	plt.xlabel('x/m')
	plt.ylabel('Intensity')
	plt.title('The Illumination Pattern at D='+str(D)+'m')
	plt.savefig('Apperture_Pattern_'+str(D)+'_'+'.pdf')
	plt.clf()
	plt.plot(x,arg_list)
	plt.xlabel('x/m')
	plt.ylabel('Relative Phase')
	plt.title('The Illumination Phase at D='+str(D)+'m')
	plt.savefig('Phase_Pattern_'+str(D)+'_.pdf')
	plt.clf()

Plot_Mag_Arg()
Plot_Mag_Arg(D=0.5)
Plot_Mag_Arg(D=0.7)
