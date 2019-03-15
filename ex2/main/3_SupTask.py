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

def Small_Del_Comp():
	apparent_period,DispA,VelA,TA = Super_Pen(init=0.20)
	apparent_period,DispB,VelB,TB = Super_Pen(init=0.20001)

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
