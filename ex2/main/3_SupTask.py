#Pendulum for 3_SupTask.py sdat2

from Super_Pen import *

### Global Variable defaults ###
h=0.05;                   # Time step
z=0.0 ## z is damping factor gamma - q was already in use
b=1 ## b = g/l
F=0 # Forcing
omega_d=2/3 # the freq of driving
initial_displacement=0.01
oscillations=170
graph_os = oscillations
sample_os = 20

def Small_Del_Comp( f= 1.2, oscillations = 170):
	apparent_period,DispA,VelA,TA = Super_Pen(init=0.20)
	apparent_period,DispB,VelB,TB = Super_Pen(init=0.20001)
	displacements = []
	velocities = []
	init_d = [0.20, 0.2001]
	for init in init_d:
		p, y, y_dot, y_t, E, E_t = Super_Pen(init= init_d,h=h, \
		                                     oscillations= oscillations,\
											 omega_d=omega_d,\
											 F = f,\
											 z = z)
		displacements.append(y)
		velocities.append(y_dot)

	for i in range(len(displacements)):
		plt.plot(y_t, displacements[i], label='Initial Displacement ='+str(init_d])+'radians')
		plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Displacement (radians)')
	plt.title('Undriven Initial Oscillations with Varied Damping')
	plt.savefig('G_Initial_Oscillations_Varied_Damping.pdf')
	plt.clf()

if True:
	plt.plot(TA,DispA,color='blue')
	plt.plot(TB,DispB,color='orange')
	plt.xlabel('Time (s)')
	plt.ylabel('Displacement (radians)')
	plt.savefig('T3_Displacement.pdf')
	plt.clf()
if True:
	plt.plot(TA,VelA,color='blue')
	plt.plot(TB,VelB,color='orange')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular velocity (rad/s)')
	plt.savefig('T3_Velocity.pdf')

print('Apparent period of oscillation (when Forcing='+str(F)+') (from sign changes of ang velocity):', apparent_period)
