#Damped simple pendulum
 
#so Hacky (np arrays are disgusting, every time you slice them they go flat)
import numpy as np
import matplotlib.pyplot as plt
                  # Initial Condition
h=0.05;                   # Time step
z=0.02 # the damping factor (q was already being used)
b=1
A = np.array([[0,1],[0,-z]])
B =np.array([[0],[1]])
maxt = 20
t = np.linspace(0,maxt,num=int(maxt/h)) 
#yexact = [1/4 + np.exp(-x)*(np.cos(x)-5/2*np.sin(x))-5/4*np.exp(-2*x) for x in t]    # Exact solution 
qstar = np.zeros((2,len(t)));
qstar[0][0]=0.1;qstar[1][0]=0 # from rest         
 # Initial condition gives solution at t=0.
k1 = np.zeros((2,1))
q1 = np.zeros((2,1))

def k_maker(q_value,time):
	return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b)

for i in range(len(t)-1):
	q0 = qstar[:,i].reshape(2,1)
	k1 = k_maker(q0,i*h)  # Approx for y gives approx for deriv
	q1 = (q0 +k1*h/2)
	k2 = k_maker(q1,i*h +h/2)
	q2 = (q0 +k2*h/2)
	k3 = k_maker(q2,i*h+h/2)
	q3 = (q0 + k3*h)
	k4 = k_maker(q3,(i+1)*h)
	qstar[:,i+1]= (q0+(k1+2*k2+2*k3+k4)*(h/6)).reshape(1,2)         # Intermediate value





#plt.plot(t,yexact,color='black')
plt.plot(t,qstar[0,:],color='blue', marker='+')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.savefig('InitialPendulum.pdf')
plt.clf()
#legend('Exact','Approximate');
