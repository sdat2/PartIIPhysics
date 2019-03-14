# A Simple Pendulum for Task1
# By sdat2

import numpy as np
import matplotlib.pyplot as plt


##### Globals
h=0.5;                   # Time step
z=0.0 ## z is damping factor gamma - q was already in use
b=1 ## b = g/l ## = w0**2 in small angle limit --> w0 = 1 rad/s --> f = 1/(2pi) Hz --> T = 2pi seconds
m=1
F=0 # no forcing in this task
omega_d=1 # not used in this task
initial_displacement=0.01 # default small initial displacement (radians)
oscillations=1000 # Number of small amplitude modelled for
number_shown = 10 # Number of oscillations shown on graph



#Coupled Differential Equations
A = np.array([[0,1],[0,-z]])
B =np.array([[0],[1]])

# global time variables
mint = (oscillations-number_shown)*2*np.pi
maxt = oscillations*2*np.pi # given that b = 1
time = np.linspace(0,maxt,num=int(maxt/h))

def y_maker(time):
	return initial_displacement*np.cos(time)
	# the theoretical value in the small angle limit

def k_maker(q_value,time):
	return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b+F*np.sin(omega_d*time))
	# Uses A and B to give the vector derivative at a point.

#lists to be filled
displacement = []
velocity = []
pend_time = []
pend_time2 = []
energy = [] # Energy by weight assuming unit length etc.

def Pendulum(init = initial_displacement):
	'''
	Function to iterate through pendulum. Returns period, alters the globals.
	'''
	#Variables needed for Runge Kutta 2
	k1 = np.zeros((2,1))
	q1 = np.zeros((2,1))
	q0 = np.zeros((2,1))
	counter = 0 # to count iterations
	clicker = 0 # to count passes through origin
	for i in time:
		if i < 0.95*h: # safely before the first time step
			q0[0][0]=init; q0[1][0]=0
		else:
			k1 = k_maker(q0,i*h)  # Approx for y gives approx for deriv
			q1 = (q0 +k1*h/2)
			k2 = k_maker(q1, i*h + h/2)
			q2 = (q0 +k2*h/2)
			k3 = k_maker(q2, i*h + h/2)
			q3 = (q0 + k3*h)
			k4 = k_maker(q3,(i+1)*h)
			q1=q0+(k1+2*k2+2*k3+k4)*(h/6)       # Calc new value
			if q1[1][0]*q0[1][0]<0: # should click once per oscillation
				clicker +=1
			q0=q1
		## Runge Kutta Method as set out in http://lpsa.swarthmore.edu/NumInt/NumIntFourth.html

		if counter%20 == 0:
			energy.append(0.5*((q0[0][0])**2) + 0.5*((q0[1][0])**2));
			pend_time2.append(i) # a time vector to go with the energy
		counter +=1
		if i > mint:
			displacement.append(q0[0][0])
			velocity.append(q0[1][0])
			pend_time.append(i)

	return (2*i)/clicker # should return the period of the simple pendulum


if True:
	#Look at a single run through a pendulum in the small angle limit.
	a= Pendulum(init = initial_displacement)
	plt.plot(pend_time2, energy, color='orange', linewidth=1)
	plt.xlabel('Time (s)')
	plt.ylabel(r'$\frac{E}{mg}$ ($m^{-1}$)')
	plt.title('Total energy over time when timestep ='+str(h)+'seconds')
	plt.savefig('C_Energy_Loss_h'+str(h)+'_.pdf')
	plt.clf()

if True:
	yexact = [y_maker(x) for x in pend_time]
	plt.plot(pend_time, yexact, color='black')
	plt.plot(pend_time, displacement, color='blue', marker='+')
	plt.xlabel('Time (s)')
	plt.ylabel('y')
	plt.savefig('A_InitialComparison.pdf')
	plt.clf()

# Look at how the frequency of the pendulum changes with initial displacement.
if True:
	theta = np.linspace(0.001, np.pi, num = 100)
	period = []
	for init_d in theta:
		 period.append(Pendulum(init=init_d))
		 print("For Initial Displacement:	" + str(init_d)+\
		       "	Period:	"+str(period[-1]) +"	seconds")
		#print("For Initial Displacement:	" + str("{:.3f}".format(init_d)))+\
			  #"	Period:	"+str("{:.3f}".format(period[-1])) +"	seconds")
	plt.plot(theta, period, color='blue', marker='+')
	plt.xlabel('Initial Displacement (radians)')
	plt.xlim([0.0,  np.pi])
	plt.ylabel('Period (seconds)')
	plt.title(r"Period vs Initial Displacement for a Pendulum "\
	           +  r" (T( $ \frac {\pi}{2} $ )="\
	           +"{:.2f}".format(Pendulum(init=np.pi/2))+" seconds)")
	plt.savefig('B_Period_Displacement.pdf')
	plt.clf()
