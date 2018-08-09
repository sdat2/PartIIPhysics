#More complicated pendulum for task1
import numpy as np
import matplotlib.pyplot as plt

h=0.05;                   # Time step
z=0.0 ## z is damping factor gamma - q was already in use
b=1 ## b = g/l ## = w0**2 in small angle limit --> w0 = 1 rad/s --> f = 1/(2pi) Hz --> T = 2pi seconds
F=0 # no forcing in this task
omega_d=1 # not used in this task 
initial_displacement=0.01
oscillations=170


A = np.array([[0,1],[0,-z]])
B =np.array([[0],[1]])

mint = (oscillations-10)*2*np.pi
maxt = oscillations*2*np.pi # given that b = 1 
t = np.linspace(0,maxt,num=int(maxt/h)) 

def y_maker(time):
	return initial_displacement*np.cos(time) # the theoretical value in the small angle limit 

def k_maker(q_value,time):
	return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b+F*np.sin(omega_d*time))
displacement = []
acceleration = []
pend_time = []
energy = [] # Energy by weight

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
			k1 = k_maker(q0,i*h)  # Approx for y gives approx for deriv
			q1 = (q0 +k1*h/2)
			k2 = k_maker(q1,i*h +h/2)
			q2 = (q0 +k2*h/2)
			k3 = k_maker(q2,i*h+h/2)
			q3 = (q0 + k3*h)
			k4 = k_maker(q3,(i+1)*h)
			q1=q0+(k1+2*k2+2*k3+k4)*(h/6)       # Intermediate value
			if q1[0][0]*q0[0][0]<0: # should click every time passes through origin
				clicker +=1 
			q0=q1

		if counter%20 == 0 and False:
			energy.append(q0[0][0]**2 +q0[1][0]**2); pend_time.append(i) 
		counter +=1
		if i > mint and False:	
			displacement.append(q0[0][0])
			acceleration.append(q0[1][0])
			pend_time.append(i)

	return (2*i)/clicker

theta = np.linspace(0.001,np.pi, num = 50)
period = []
print(Pendulum(init=np.pi/2))
if True:
	for init_d in theta:
		 period.append(Pendulum(init=init_d))
	plt.plot(theta,period,color='blue',marker='+')
	plt.xlabel('Initial Displacement (radians)')
	plt.ylabel('Period (seconds)')
	
	plt.title('Period vs Initial Displacement for a Pendulum (T(pi/2)='+"{:.2f}".format(Pendulum(init=np.pi/2))+' seconds) ')
	plt.savefig('Period_Displacement.pdf')
	plt.clf()
	
if False:
	a = Pendulum()

if False:
	yexact = [y_maker(x) for x in pend_time]
	plt.plot(pend_time,yexact,color='black')
	plt.plot(pend_time,displacement,color='blue', marker='+')
	plt.xlabel('Time (s)')
	plt.ylabel('y')
	plt.savefig('Task1Pendulum.pdf')

if False:
	plt.plot(pend_time,energy,color='orange')
	plt.xlabel('Time (s)')
	plt.ylabel('Energy/(mass*g) (m^{-1})')
	plt.title('Energy loss over time when timestep ='+str(h)+'seconds')
	plt.savefig('Energy_Loss_h'+str(h)+'_.pdf')
	plt.clf()
#legend('Exact','Approximate');
