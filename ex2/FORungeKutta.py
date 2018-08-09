#Exammple 1
# Solve y'(t)=-2y(t) with y0=3, midpoint method
import numpy as np
import matplotlib.pyplot as plt

y0 = 3;                  # Initial Condition
h=0.2;                   # Time step
t = np.linspace(0,2,num=int(2/h)) 
yexact = [3*np.exp(-2*x) for x in t]    # Exact solution 
ystar = np.zeros(len(t));
ystar[0] = y0;           # Initial condition gives solution at t=0.
for i in range(len(t)-1):
	k1 = -2*ystar[i]              # Approx for y gives approx for deriv
	y1 = ystar[i]+k1*h/2;         # Intermediate value
	k2 = -2*y1                    # Approx deriv at intermediate value.
	ystar[i+1] = ystar[i] + k2*h; # Approximate solution at next value of y
plt.plot(t,yexact,color='black')
plt.plot(t,ystar,color='blue', marker='+')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.savefig('FirstOrder.pdf')
plt.clf()
#legend('Exact','Approximate');
