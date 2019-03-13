#program for task 3 by sdat2 drawing on
# http://kmdouglass.github.io/posts/approximating-diffraction-patterns-of-rectangular-apertures-with-the-fft.html
# Usage 3_Task3.py [number of bins] [wavelength] [slit width] [Apperture Width]
# [propogation distance (microns)] [ x limit]

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import fftshift, ifftshift
import sys

#The sinc function
def sinc(x):
    if (x != 0): # Prevent divide-by-zero
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
AppertureWidth = 100000 # microns
m=8
s=100
sinusoidal=False
plt_theory=False
x_lim = 20000

#redefine by Command Line
if len(sys.argv)>1: bins = int(sys.argv[1])
if len(sys.argv)>2: wavelength = float(sys.argv[2])
if len(sys.argv)>3: slitWidth = float(sys.argv[3])
if len(sys.argv)>4: AppertureWidth = int(sys.argv[4])
if len(sys.argv)>5: propDistance = float(sys.argv[5])
if len(sys.argv)>6: x_lim  = float(sys.argv[6])

# Create Space
x     = np.linspace(-AppertureWidth/2, AppertureWidth/2, num = bins)
field = np.zeros(x.size, dtype='complex128') # Field complex
newfield = np.zeros(x.size,dtype='complex128')

# Changes Phase
def phase(x):
    return m/2*np.sin(2*np.pi*x/s)
for i in range(len(x)):
    if x[i] > -slitWidth / 2 and x[i] <= slitWidth / 2:
        if sinusoidal:
            field[i] = amplitude*(np.cos(phase(x[i])) + np.sin(phase(x[i]))*1j)
        else:
            field[i]=amplitude + 0j
        newfield[i]=field[i]*np.exp(1j*np.pi*(x[i]**2)/(wavelength*propDistance))


#creates an apperture of the correct width and amp of 1
dx = x[1] - x[0] # Spatial sampling period, microns
fS = 1 / dx      # Spatial sampling frequency, units are inverse microns
f  = (fS / x.size) * np.arange(0, x.size, step = 1) # a frequency type vector

###########ACTUAL FFT#####################
diffractedField = dx * np.fft.fft(field) # take the FFT of the apperture function
newdiffractedField = dx * np.fft.fft(newfield)
# fftshift uses the symmetry of the appeture to get rid of negative part

####### Rescaling ##########
xPrime   = np.hstack((f[-int((f.size/2)):] - fS, f[0:int(f.size/2)])) * wavelength * propDistance
IntensTheory = amplitude / (wavelength * propDistance) * \
    (slitWidth * sinc(xPrime * slitWidth / wavelength / propDistance))**2
IntensFFT    = np.fft.fftshift(diffractedField * np.conj(diffractedField))\
               / wavelength / propDistance
newIntensFFT = np.fft.fftshift(newdiffractedField * np.conj(newdiffractedField))\
               / wavelength / propDistance

####### Plotting #########
plt.plot(xPrime, np.abs(IntensFFT), label = 'FFT (Uncorrected)')
plt.plot(xPrime, np.abs(newIntensFFT), label = 'FFT (Corrected)')
if plt_theory: plt.plot(xPrime, IntensTheory, label = 'Simple slit of equal width')
plt.xlim((-x_lim , x_lim))
plt.xlabel(r'x-position, $\mu m$')
plt.ylabel(r'Power density, $V^2 / \mu m$')
plt.grid(True)
plt.legend()
plt.savefig('Task3_Output/Task3_lam='+str(wavelength)+'_d='+str(slitWidth)+'_D='\
            +str(propDistance)+'_microns.pdf')
