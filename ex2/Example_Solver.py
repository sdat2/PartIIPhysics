import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def deriv(u, t):
    return np.array([u[1], -u[0] + np.sqrt(u[0])])

time = np.arange(0.01, 7 * np.pi, 0.0001) #Create a clear range of times
uinit = np.array([1.49907, 0]) # initial conditions?
u = odeint(deriv, uinit, time) # integrate

x = 1 / u[:, 0] * np.cos(time) # scaling
y = 1 / u[:, 0] * np.sin(time)

plt.plot(x, y) # scale
plt.show()
