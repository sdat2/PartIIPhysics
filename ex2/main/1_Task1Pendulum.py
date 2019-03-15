# A Simple Pendulum for Task1

from Super_Pen import *

def displacement_plotter(h=0.05, oscillations= 10):
    p, y, y_dot, y_t, E, E_t = Super_Pen(h=h, oscillations= oscillations)
    yexact = [y_maker(x) for x in y_t]
    plt.plot(y_t, yexact, color='black')
    plt.plot(y_t, y, color='blue', marker='+')
    plt.xlabel('Time (s)')
    plt.ylabel('y')
    plt.savefig('A_Undamped_h='+str(h)+'_Displacment.pdf')
    plt.clf()
    return 0

#displacement_plotter(h=0.05, oscillations= 10)
#displacement_plotter(h=0.5, oscillations= 10)
#displacement_plotter(h=1, oscillations= 10)

def energy_plotter(h_vec=[0.01,0.05,0.1,0.12,0.13], oscillations= 1000, os_sampled=1000):
    for h in h_vec:
        p, y, y_dot, y_t, E, E_t = Super_Pen(h=h, oscillations= oscillations)
        plt.plot(E_t, E/(E[0]),label='Timestep = '+str(h)+' seconds',\
                 linewidth=1)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Percentage of Initial Energy %')
    plt.title('Total Energy over Time for '+str(oscillations)+' Oscillations')
    plt.savefig('C_Energy.pdf')
    plt.clf()

#energy_plotter()

def period_vs_init(num=50, h=0.05, oscillations=100):
	theta = np.linspace(0.001, np.pi-0.001, num = num)
	period = []
	p0, y, y_dot, y_t, E, E_t = Super_Pen(init= np.pi/2,h=h, oscillations=oscillations)
	for init_d in theta:
		p, y, y_dot, y_t, E, E_t = Super_Pen(init= init_d,h=h, oscillations= oscillations)
		period.append(p)
		print("For Initial Displacement:	" + str(init_d)+\
		      "	Period:	"+str(period[-1]) +"	seconds")
	plt.plot(theta, period, color='blue', marker='+')
	plt.xlabel('Initial Displacement (radians)')
	plt.xlim([0.0,  np.pi])
	plt.ylabel('Period (seconds)')
	plt.title(r"Period vs Initial Displacement for a Pendulum "\
	          +  r" (T( $ \frac {\pi}{2} $ )="\
			  +"{:.2f}".format(p0)+" seconds)")
	plt.savefig('B_Period_Displacement.pdf')
	plt.clf()

period_vs_init()
