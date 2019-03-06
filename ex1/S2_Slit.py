'''
Cornu Integration Program for ST2
by sdat2
'''

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
        '''
        Integrates a 2-d slit.
        '''
        Scaling = (2/(lam*D))**0.5
        u2 = x1*Scaling; u1 = x0*Scaling
        #print('u2 = ', u2, 'u1 = ', u1)
        imag1,real1 = Integrator(u1)
        imag2,real2 = Integrator(u2)
        imag = -imag1+imag2
        real = -real1+real2
        mag = (imag**2+real**2)*0.5
        arg = np.arctan(imag/real)
        return mag, arg


def Plot_Mag_Arg(d=0.1, lam=0.01, D=0.3):
        '''
        Runs the Two_ended function for different parameters 
        and plots the result.
        '''
        mag_list = []; arg_list =[]
        x = np.linspace(-0.05,0.05,num=1000)
        for i in x:
            mag, arg = Two_Ended(i, i+d, D=D, lam=lam)
            mag_list.append(mag); arg_list.append(arg)
        # Plot the magnitudes.
        plt.plot(x,mag_list)
        plt.xlabel('x/m')
        plt.ylabel('Intensity')
        plt.title('The Illumination Pattern at D='+str(D)+'m')
        plt.savefig('D_Apperture_Pattern_'+str(D)+'_'+'.pdf')
        plt.clf()
        # Plot the phases.
        plt.plot(x,arg_list)
        plt.xlabel('x/m')
        plt.ylabel('Relative Phase')
        plt.title('The Illumination Phase at D='+str(D)+'m')
        plt.savefig('E_Phase_Pattern_'+str(D)+'_.pdf')
        plt.clf()

######## Differnt Inputs #######
Plot_Mag_Arg()
Plot_Mag_Arg(D=0.5)
Plot_Mag_Arg(D=0.7)
