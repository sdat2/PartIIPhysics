#Pendulum for task2 by sdat2
#Usage: 2_Task2Pendulum.py [damping coeff] [forcing coeff] [timestep] [oscillations modelled]
#Example: 2_Task2Pendulum.py 0.5 0.5 0.1 10

import numpy as np
import matplotlib.pyplot as plt
import sys


### Global Variable defaults ###
h=0.05;                   # Time step
z=0.0 ## z is damping factor gamma - q was already in use
b=1 ## b = g/l
F=0 # Forcing
omega_d=2/3 # the freq of driving
initial_displacement=0.01
oscillations=170
graph_os = 10
sample_os = 20

### Command Line Inputs ###
if len(sys.argv) >1: z = float(sys.argv[1])
if len(sys.argv) >2: F = float(sys.argv[2])
if len(sys.argv) >3: h = float(sys.argv[3])
if len(sys.argv) >4: oscillations = int(sys.argv[4])
if len(sys.argv) >5: graph_os = int(sys.argv[5])
if len(sys.argv) >6: sample_os = int(sys.argv[6])


#Matrices from solving 2nd order ODE
A = np.array([[0,1],[0,-z]])
B =np.array([[0],[1]])

#it is only ever useful to plot about 10 oscillations worth
mint = (oscillations-graph_os)*2*np.pi
mint2=(oscillations -sample_os)*2*np.pi
maxt = oscillations*2*np.pi # given that b = 1
t = np.linspace(0,maxt,num=int(maxt/h))

#sometimes it is useful to compare to perfect SHM
def y_maker(time):
	return initial_displacement*np.cos(time)

def k_maker(q_value,time): #(Otherwise known as the derivative!)
	return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b+F*np.sin(omega_d*time))

displacement = []
velocity = []
pend_time = []


def Pendulum(init=initial_displacement):
	k1 = np.zeros((2,1))
	q1 = np.zeros((2,1))
	q0 = np.zeros((2,1))
	counter = 0
	clicker = 0
	for i in t:
		if i < 0.95*h:
			q0[0][0]=init; q0[1][0]=0
		else:
			k1 = k_maker(q0,i)  # Approx for y gives approx for deriv
			q1 = (q0 +k1*h/2)
			k2 = k_maker(q1,i +h/2)
			q2 = (q0 +k2*h/2)
			k3 = k_maker(q2,i+h/2)
			q3 = (q0 + k3*h)
			k4 = k_maker(q3,i*h)
			q1=q0+(k1+2*k2+2*k3+k4)*(h/6)       # Intermediate value
			if q1[1][0]*q0[1][0]<0 and i >mint2: # should click every time passes through origin
				clicker +=1
			q0=q1

		counter +=1
		if i > mint:
			displacement.append(q0[0][0])
			velocity.append(q0[1][0])
			pend_time.append(i)
	return (2*(i-mint2))/clicker


if True:
	apparent_period = Pendulum(init=initial_displacement)

if True:
	#yexact = [y_maker(x) for x in pend_time]
	#plt.plot(pend_time,yexact,color='black')
	plt.plot(pend_time,displacement,color='blue')
	plt.xlabel('Time (s)')
	plt.ylabel('Displacement (radians)')
	plt.savefig('T2Displacement_'+str(F)+'_Forcing.pdf')
	plt.clf()
if True:
	plt.plot(pend_time,velocity,color='blue')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular velocity (rad/s)')
	plt.savefig('T2Velocity_'+str(F)+'_Forcing.pdf')

print('Apparent period of oscillation (when Forcing='+str(F)+') (from sign changes of ang velocity):', apparent_period)