from Super_Pen import *


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





def period_vs_forcing(init_d = 0.01, num= 10, h=0.05, omega_d=2/3, \
                      oscillations=1000,z=0.5, os_shown=30):
	f_vec = [0.5, 1.2, 1.44, 1.465]
	period = []
	displacements = []
	velocities = []
	for f in f_vec:
		p, y, y_dot, y_t, E, E_t = Super_Pen(init= init_d,h=h, \
		                                     oscillations= oscillations,\
											 os_sampled= oscillations/2,\
											 omega_d=omega_d,\
											 F = f,\
											 z = z)
		period.append(p)
		displacements.append(y)
		velocities.append(y_dot)
		print("Forcing:	" + str(f)+"	Period:	"+str(period[-1]) +"	seconds")
	plt.plot(f_vec, period, color='blue', marker='+')
	plt.xlabel('Forcing')
	plt.xlim([0.0,  np.pi])
	plt.ylabel('Period (seconds)')
	plt.title(r"Apparent Period vs Forcing for an Undamped Pendulum in steady state")
	plt.savefig('D_Forcing_Period_q0.5_Steady_State.pdf')
	plt.clf()
	for i in range(len(displacements)):
		plt.plot(y_t, displacements[i], label='F ='+str(f_vec[i])+'')
	plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Displacement (Radians)')
	plt.title('Steady State Forced Oscillations with q=0.5 ')
	plt.savefig('E_Forcing_Displacement_q0.5_Steady_State.pdf')
	plt.clf()
	for i in range(len(displacements)):
		plt.plot(y_t, velocities[i], label='F ='+str(f_vec[i])+'')
	plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Velocity (Radians per Second)')
	plt.title('Steady State Forced Oscillations with q=0.5 ')
	plt.savefig('F_Forcing_Angular_Velocity_q0.5_Steady_State.pdf')
	plt.clf()

period_vs_forcing()

def displacement_vs_damping(init_d = 0.01, num= 100, h=0.05, omega_d=0, \
                      oscillations=10, z=0.5, f=0):
	z_vec = [0,1,5,10]
	period = []
	displacements = []
	for z in z_vec:
		p, y, y_dot, y_t, E, E_t = Super_Pen(init= init_d,h=h, \
		                                     oscillations= oscillations,\
											 omega_d=omega_d,\
											 F = f,
											 z=z)
		displacements.append(y)
	for i in range(len(displacements)):
		plt.plot(y_t, displacements[i], label='q ='+str(z_vec[i])+'')
		plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Displacement (radians)')
	plt.title('Undriven Initial Oscillations with Varied Damping')
	plt.savefig('G_Initial_Oscillations_Varied_Damping.pdf')
	plt.clf()


displacement_vs_damping()
