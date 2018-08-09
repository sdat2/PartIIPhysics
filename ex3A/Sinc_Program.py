import numpy as np
import matplotlib.pyplot as plt

# Create a sinc function to operate on numpy arrays
def sinc(x):
    if (x != 0):
        # Prevent divide-by-zero
        return np.sin(np.pi * x) / (np. pi * x)
    else:
        return 1
sinc = np.vectorize(sinc)

amplitude    = 1     # Volt / sqrt(micron)
slitWidth    = 5     # microns
wavelength   = 0.532 # microns
propDistance = 10000 # microns (= 10 mm)

x = np.arange(-10000, 10000, 1)
F = sinc(slitWidth * x / wavelength / propDistance)
I = amplitude / (wavelength * propDistance) * (slitWidth * F)**2

plt.plot(x, I, linewidth = 2)
plt.xlim((-5000, 5000))
plt.xlabel(r'Position in observation plane, $\mu m$')
plt.ylabel('Power density, $V^2 / \mu m$')
plt.grid(True)
plt.savefig('Sinc.pdf')
plt.clf()
