#Exammple 4
# Solve y'''(t)+4y''+6y'+4=gamma(t), Euler method, 
#so Hacky (np arrays are disgusting, every time you slice them they go flat)
import numpy as np
import matplotlib.pyplot as plt

q0 = np.array([[0],[-1],[0]])                  # Initial Condition
h=0.05;                   # Time step
A = np.array([[0,1,0],[0,0,1],[-4,-6,-4]])
B =np.array([[0],[0],[1]])
t = np.linspace(0,5,num=int(5/h)) 
yexact = [1/4 + np.exp(-x)*(np.cos(x)-5/2*np.sin(x))-5/4*np.exp(-2*x) for x in t]    # Exact solution 
qstar = np.zeros((3,len(t)));
qstar[0][0]=q0[0][0];qstar[1][0]=q0[1][0];qstar[2][0]=q0[2][0];          
 # Initial condition gives solution at t=0.
k1 = np.zeros((3,1))
q1 = np.zeros((3,1))
for i in range(len(t)-1):
	k1 = A.dot(qstar[:,i]).reshape(3,1)+B  # Approx for y gives approx for deriv
	q1 = (qstar[:,i].reshape(3,1) +k1*h/2)
	k2 = A.dot(q1)+B
	q2 = (qstar[:,i].reshape(3,1) +k2*h/2)
	k3 = A.dot(q2)+B
	q3 = (qstar[:,i].reshape(3,1)+k3*h)
	k4 = A.dot(q3)+B
	qstar[:,i+1]= (qstar[:,i].reshape(3,1)+(k1+2*k2+2*k3+k4)*(h/6)).reshape(1,3)         # Intermediate value

	#k2 = q1*(1-2*(t[i]+h/2))                    # Approx deriv at intermediate value.
	#ystar[i+1] = ystar[i] + k1*h; # Approximate solution at next value of y
plt.plot(t,yexact,color='black')
plt.plot(t,qstar[0,:],color='blue', marker='+')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.savefig('FourthOMatrix.pdf')
plt.clf()
#legend('Exact','Approximate');
