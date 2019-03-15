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

def Small_Del_Comp( f= 1.2, oscillations = 170, z=0.5):
	displacements = []
	velocities = []
	init_d = [0.20, 0.2001]
	for init in init_d:
		p, y, y_dot, y_t, E, E_t = Super_Pen(init=init,h=h, \
		                                     oscillations= oscillations,\
											 omega_d=omega_d,\
											 F = f,\
											 z = z)
		displacements.append(y)
		velocities.append(y_dot)

	for i in range(len(displacements)):
		plt.plot(y_t, displacements[i], label='Initial Displacement ='+str(init_d[i])+' radians')
		plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Displacement (radians)')
	plt.title('Driven Oscillations for 170 Oscilliations')
	plt.savefig('H_Small_Init_Diff_Change_Displacements.pdf')
	plt.clf()
	for i in range(len(velocities)):
		plt.plot(y_t, velocities[i], label='Initial Displacement ='+str(init_d[i])+' radians')
		plt.legend()
	plt.xlabel('Time (seconds)')
	plt.ylabel('Angular Velocity (radians per second)')
	plt.title('Driven Oscillations for 170 Oscilliations')
	plt.savefig('I_Small_Init_Diff_Change_Velocities.pdf')
	plt.clf()

Small_Del_Comp()
