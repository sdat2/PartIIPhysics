import numpy as np
import matplotlib.pyplot as plt

def y_maker(time, initial_displacement=0.01):#( theoretical small angle limit)
    return initial_displacement*np.cos(time)

def k_maker(q_value,time,z=0,F=0, b=1, omega_d=2/3):#(Otherwise known as the derivative!)
    A = np.array([[0,1],[0,-z]])
    B =np.array([[0],[1]])
    return A.dot(q_value)+B*(-np.sin(q_value[0][0])*b+F*np.sin(omega_d*time))

def Super_Pen(h=0.5,b=1, m=1, F=0, omega_d=2/3, init=0.01, \
              oscillations=1000, os_shown = 10, os_sampled = 1000, z = 0):
    '''
	Function to iterate through pendulum. Returns period, and other tracked
    variables. It is only ever useful to plot about 10 oscillations worth
	'''
    mint = (oscillations-os_shown)*2*np.pi
    mint2=(oscillations -os_sampled )*2*np.pi
    maxt = oscillations*2*np.pi # given that b = 1
    t = np.linspace(0,maxt,num=int(maxt/h))
    #Variables for return
    disp = []; vel = []; pend_time = []; energy_time = []; energy = []
    #Variables needed for Runge Kutta 2
    k1 = np.zeros((2,1))
    q1 = np.zeros((2,1))
    q0 = np.zeros((2,1))
    counter = 0 # to count iterations
    clicker = 0 # to count passes through origin
    for i in t:
        if i < 0.95*h:
            q0[0][0]=init; q0[1][0]=0
        else:
            k1 = k_maker(q0,i,z=z,F=F, b=b, omega_d=omega_d)
            q1 = (q0 +k1*h/2)
            k2 = k_maker(q1,i +h/2,z=z,F=F, b=b, omega_d=omega_d)
            q2 = (q0 +k2*h/2)
            k3 = k_maker(q2,i+h/2,z=z,F=F, b=b, omega_d=omega_d)
            q3 = (q0 + k3*h)
            k4 = k_maker(q3,i*h,z=z,F=F, b=b, omega_d=omega_d)
            q1=q0+(k1+2*k2+2*k3+k4)*(h/6)       # Intermediate value # should click every time passes through origin
            if q1[1][0]*q0[1][0]<0 and i >mint2: # multiply velocities together
                clicker +=1
            q0=q1
        ## Runge Kutta Method as set out in http://lpsa.swarthmore.edu/NumInt/NumIntFourth.html
        if counter%1 == 0 and i > mint2:
            energy.append(0.5*((q0[0][0])**2) + 0.5*((q0[1][0])**2));
            energy_time.append(i) # a time vector to go with the energy
            counter +=1
        if i > mint:
            disp.append(q0[0][0])
            vel.append(q0[1][0])
            pend_time.append(i)
    period = (2*i)/clicker # should return the period of the simple pendulum
    return period, disp, vel, pend_time, energy, energy_time
