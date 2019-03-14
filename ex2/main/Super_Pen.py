import numpy as np

def Super_Pen(h=0.5,b=1, m=1, F=0, omega_d=2/3, initial_displacement=0.01, \
              oscillations=1000, number_shown = 10):
	'''
	Function to iterate through pendulum. Returns period, alters the globals.
	'''
    def k_maker(q_value,time,z=z,F=F): #(Otherwise known as the derivative!)
    	A = np.array([[0,1],[0,-z]])
    	B =np.array([[0],[1]])
    	return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b+F*np.sin(omega_d*time))

    def y_maker(time):
    	return initial_displacement*np.cos(time)

    #it is only ever useful to plot about 10 oscillations worth
    mint = (oscillations-graph_os)*2*np.pi
    mint2=(oscillations -sample_os)*2*np.pi
    maxt = oscillations*2*np.pi # given that b = 1
    t = np.linspace(0,maxt,num=int(maxt/h))

    #Variables for return
	displacement = []
	velocity = []
	pend_time = []
    energy_time = []
    energy = []

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

	period = (2*i)/clicker # should return the period of the simple pendulum

    return period, disp, vel, pend_time, energy, vel, energy_time


def Displacement_Plotter(name='Displacement'):

    return 0

def Energy_Plotter():

    return 0
