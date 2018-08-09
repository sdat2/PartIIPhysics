import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import fftshift, ifftshift
import sys


def sinc(x):
    if (x != 0):
        # Prevent divide-by-zero
        return np.sin(np.pi * x) / (np. pi * x)
    else:
        return 1
sinc = np.vectorize(sinc)


amplitude    = 1     # Volt / sqrt(micron)
slitWidth    = 100     # microns
wavelength   = 0.5 # microns
propDistance = 10**6 # microns (= 1 mm)
bins = 2048
AppertureWidth = 5000

if len(sys.argv)>1: bins = int(sys.argv[1])
if len(sys.argv)>2: wavelength = float(sys.argv[2])
if len(sys.argv)>3: slitwidth = float(sys.argv[3])
if len(sys.argv)>4: AppertureWidth = int(sys.argv[4])
if len(sys.argv)>5: propogation_distance = float(sys.argv[5])


x     = np.linspace(-AppertureWidth/2, AppertureWidth/2, num = bins)
field = np.zeros(x.size, dtype='complex128') # Ensure the field is complex

field[np.logical_and(x > -slitWidth / 2, x <= slitWidth / 2)] = amplitude + 0j
#creates an apperture of the correct width and amp of 1

plt.plot(x, np.abs(field), '.')
plt.xlabel(r'x-position, $\mu m$')
plt.ylabel(r'Field amplitude, $V / \sqrt{\mu m}$')
plt.ylim((0, 1))
plt.grid(True)
plt.savefig('Single_Slit_Appeture.pdf')
plt.clf()

dx = x[1] - x[0] # Spatial sampling period, microns
fS = 1 / dx      # Spatial sampling frequency, units are inverse microns
f  = (fS / x.size) * np.arange(0, x.size, step = 1) # inverse microns
# an frequency type vector the same size as the apperture function

#diffractedField = dx * fft(fftshift(field)) # The field must be rescaled by dx to get the correct units
###########ACTUAL FFT#####################
diffractedField = dx * np.fft.fft(np.fft.fftshift(field)) # take the FFT of the apperture function
# fftshift uses the symmetry of the appeture to get rid of negative part

# Plot the field up to the Nyquist frequency, fS / 2
plt.plot(f[f <= fS / 2], np.abs(diffractedField[f <= fS / 2]), '.', linewidth = 2)
plt.xlim((0, fS / 2))
plt.xlabel(r'Spatial frequency, $\mu m^{-1}$')
plt.ylabel(r'Field amplitude, $V / \sqrt{\mu m}$')
plt.grid(True)
if False: plt.savefig('Spatial_Frequency.pdf')
plt.clf()

xPrime   = np.hstack((f[-int((f.size/2)):] - fS, f[0:int(f.size/2)])) * wavelength * propDistance

IrradTheory = amplitude / (wavelength * propDistance) * \
    (slitWidth * sinc(xPrime * slitWidth / wavelength / propDistance))**2

IrradFFT    = np.fft.fftshift(diffractedField * np.conj(diffractedField)) / wavelength / propDistance

plt.plot(xPrime, np.abs(IrradFFT), '.', label = 'FFT')
plt.plot(xPrime, IrradTheory, label = 'Theory')
plt.xlim((-20000, 20000))
plt.xlabel(r'x-position, $\mu m$')
plt.ylabel(r'Power density, $V^2 / \mu m$')
plt.grid(True)
plt.legend()
plt.savefig('Comparison_.pdf')
