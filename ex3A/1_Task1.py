#program for task 1 by sdat2 drawing on
# http://kmdouglass.github.io/posts/approximating-diffraction-patterns-of-rectangular-apertures-with-the-fft.html
# Usage 1_Task1.py [number of bins] [wavelength] [slit width] [Apperture Width]
# [propogation distance (microns)]


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
slitWidth    = 100     # microns
wavelength   = 0.5 # microns
propDistance = 10**6 # microns (= 1 mm)
bins = 2048
AppertureWidth = 5000 # microns

#redefine by Command Line
if len(sys.argv)>1: bins = int(sys.argv[1])
if len(sys.argv)>2: wavelength = float(sys.argv[2]) # microns
if len(sys.argv)>3: slitwidth = float(sys.argv[3]) # microns
if len(sys.argv)>4: AppertureWidth = int(sys.argv[4]) # microns
if len(sys.argv)>5: propogation_distance = float(sys.argv[5]) # microns


x     = np.linspace(-AppertureWidth/2, AppertureWidth/2, num = bins)
field = np.zeros(x.size, dtype='complex128') # Field complex
field[np.logical_and(x > -slitWidth / 2, x <= slitWidth / 2)] = amplitude + 0j

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
plt.plot(xPrime, IntensTheory, label = 'Theory')
plt.xlim((-20000, 20000))
plt.xlabel(r'x-position, $\mu m$')
plt.ylabel(r'Power density, $V^2 / \mu m$')
plt.grid(True)
plt.legend()
plt.savefig('Task1_lam='+str(wavelength)+'_d='+str(slitWidth)+'_D='+str(AppertureWidth)+'_microns.pdf')
