#Exammple 1
# Solve y'(t)=y(t)(1-2t) with y0=3, midpoint method
import numpy as np
import matplotlib.pyplot as plt

y0 = 3;                  # Initial Condition
h=0.2;                   # Time step
t = np.linspace(0,2,num=int(2/h)) 
yexact = [3*np.exp(x-x**2) for x in t]    # Exact solution 
ystar = np.zeros(len(t));
ystar[0] = y0;           # Initial condition gives solution at t=0.
for i in range(len(t)-1):
	k1 = ystar[i]*(1-2*t[i])              # Approx for y gives approx for deriv
	y1 = ystar[i]+k1*h/2         # Intermediate value
	k2 = y1*(1-2*(t[i]+h/2))                    # Approx deriv at intermediate value.
	y2 = ystar[i]+k2*h/2
	k3 = y2*(1-2*(t[i]+h/2))
	y3 = ystar[i] + k3*h
	k4 = y2*(1-2*(t[i]+h))
	ystar[i+1] = ystar[i] + (k1+2*k2+2*k3+k4)*h/6; # Approximate solution at next value of y
plt.plot(t,yexact,color='black')
plt.plot(t,ystar,color='blue', marker='+')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.savefig('FourthOrder.pdf')
plt.clf()
#legend('Exact','Approximate');
