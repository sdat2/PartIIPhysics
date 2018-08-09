#program for task 2 by sdat2 drawing on
# http://kmdouglass.github.io/posts/approximating-diffraction-patterns-of-rectangular-apertures-with-the-fft.html

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

#globals
amplitude    = 1     # Volt / sqrt(micron)
slitWidth    = 2000     # microns
wavelength   = 0.5 # microns
propDistance = 10*10**6 # microns (= 10 m)
bins = 2048
AppertureWidth = 100000
m=8
s=100

#redefine by Command Line
if len(sys.argv)>1: bins = int(sys.argv[1])
if len(sys.argv)>2: wavelength = float(sys.argv[2])
if len(sys.argv)>3: slitwidth = float(sys.argv[3])
if len(sys.argv)>4: AppertureWidth = int(sys.argv[4])
if len(sys.argv)>5: propogation_distance = float(sys.argv[5])


x     = np.linspace(-AppertureWidth/2, AppertureWidth/2, num = bins)
field = np.zeros(x.size, dtype='complex128') # Field complex

def phase(x):
    return m/2*np.sin(2*np.pi*x/s)
for i in range(len(x)):
    if x[i] > -slitWidth / 2 and x[i] <= slitWidth / 2:
        field[i] = amplitude*(np.cos(phase(x[i])) + np.sin(phase(x[i]))*1j)
#creates an apperture of the correct width and amp of 1
dx = x[1] - x[0] # Spatial sampling period, microns
fS = 1 / dx      # Spatial sampling frequency, units are inverse microns
f  = (fS / x.size) * np.arange(0, x.size, step = 1) # a frequency type vector
###########ACTUAL FFT#####################
diffractedField = dx * np.fft.fft(np.fft.fftshift(field)) # take the FFT of the apperture function
# fftshift uses the symmetry of the appeture to get rid of negative part

xPrime   = np.hstack((f[-int((f.size/2)):] - fS, f[0:int(f.size/2)])) * wavelength * propDistance
IntensTheory = amplitude / (wavelength * propDistance) * \
    (slitWidth * sinc(xPrime * slitWidth / wavelength / propDistance))**2
IntensFFT    = np.fft.fftshift(diffractedField * np.conj(diffractedField)) / wavelength / propDistance

plt.plot(xPrime, np.abs(IntensFFT), '.', label = 'FFT')
plt.plot(xPrime, IntensTheory, label = 'Simple slit of equal width')
plt.xlim((-20000, 20000))
plt.xlabel(r'x-position, $\mu m$')
plt.ylabel(r'Power density, $V^2 / \mu m$')
plt.grid(True)
plt.legend()
plt.savefig('Task2_lam='+str(wavelength)+'_d='+str(slitWidth)+'_D='+str(AppertureWidth)+'_microns.pdf')
