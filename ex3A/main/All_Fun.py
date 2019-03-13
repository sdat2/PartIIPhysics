#program for Ex3A by sdat2 drawing on
# http://kmdouglass.github.io/posts/approximating-diffraction-patterns-of-rectangular-apertures-with-the-fft.html
# Go to the bottom of the script to add new function calls

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import fftshift, ifftshift

#The sinc function
def sinc(x, offset = 0):
    if (x - offset != 0): # Prevent divide-by-zero
        return np.sin(np.pi * x) / (np. pi * x)
    else:
        return 1
sinc = np.vectorize(sinc)



def FFT_Intensity(amplitude=1, slitWidth=2000, wavelength=0.5,\
                  propDistance=10*10**6, bins=2048, AppertureWidth=100000,\
                  m=8, s=100,sinusoidal=False, plt_theory=True, x_lim = 20000,\
                  Task = 3):
    '''
    This function contains all the code for all 3 tasks, including plotting.
    Not the best design, but better than the 3 free form scripts with globals
    and command line prompts I was using previously.
    '''
    #### Phase for Task 2.
    def phase(x):
        return m/2*np.sin(2*np.pi*x/s)

    # Create Space
    x     = np.linspace(-AppertureWidth/2, AppertureWidth/2, num = bins)
    field = np.zeros(x.size, dtype='complex128') # Field complex
    newfield = np.zeros(x.size,dtype='complex128')

    if Task == 1:
        field[np.logical_and(x > -slitWidth / 2,\
              x <= slitWidth / 2)] = amplitude + 0j
    else:
        for i in range(len(x)):
            if x[i] > -slitWidth / 2 and x[i] <= slitWidth / 2:
                if sinusoidal:
                    field[i] = amplitude*(np.cos(phase(x[i])) + np.sin(phase(x[i]))*1j)
                else:
                    field[i]=amplitude + 0j
                #### Add Phase Factor Required by Task 3 ####
                if Task == 3:
                    newfield[i]=field[i]*np.exp((1j*np.pi*(x[i]**2))/(wavelength*propDistance))

    ######### Useful FFT Variables #########
    dx = x[1] - x[0] # Spatial sampling period, microns
    fS = 1 / dx      # Spatial sampling frequency, units are inverse microns
    f  = (fS / x.size) * np.arange(0, x.size, step = 1) # a frequency type vector

    ###########ACTUAL FFT#####################
    if  Task == 1:
        diffractedField = dx * np.fft.fft(np.fft.fftshift(field))
    else:
        diffractedField = dx * np.fft.fft(field)
        # take the FFT of the apperture function
    #Deal with corrected version ###
    if Task == 3:
        newdiffractedField = dx * np.fft.fft(newfield)
    # fftshift uses the symmetry of the appeture to get rid of negative part

    ####### Rescaling ##########
    xPrime   = np.hstack((f[-int((f.size/2)):] - fS, f[0:int(f.size/2)]))\
               * wavelength * propDistance #
    IntensTheory = amplitude / (wavelength * propDistance) * \
        (slitWidth * sinc(xPrime * slitWidth / wavelength / propDistance))**2

    ###########FURTHER FFT#####################
    IntensFFT    = np.fft.fftshift(diffractedField * np.conj(diffractedField))\
                   / wavelength / propDistance #
    if Task == 3:
        newIntensFFT = np.fft.fftshift(newdiffractedField * np.conj(newdiffractedField))\
                       / wavelength / propDistance

    ####### Plotting #########
    if Task == 1:
        plt.plot(xPrime, np.abs(IntensFFT), '.', label = 'FFT')
        plt.plot(xPrime, IntensTheory, label = 'Theory')

    if Task == 2:
        plt.plot(xPrime, np.abs(IntensFFT), '.', label = 'FFT for Sinusoidal Phase Apperture')
        if plt_theory: plt.plot(xPrime, IntensTheory, label = 'Simple slit of equal width')

    if Task == 3:
        plt.plot(xPrime, np.abs(IntensFFT), label = 'FFT (Uncorrected)')
        plt.plot(xPrime, np.abs(newIntensFFT), label = 'FFT (Corrected)')
        if plt_theory: plt.plot(xPrime, IntensTheory, label = 'FT Theory')

    plt.xlim((-x_lim , x_lim))
    plt.xlabel(r'Screen Position, $\mu m$')
    plt.ylabel(r'Intensity on Screen, $V^2 / \mu m$')
    plt.grid(True)
    plt.legend()
    plt.savefig('Task'+str(Task)+'_lam='+str(wavelength)+\
               '_d='+str(slitWidth)+'_Sinusoidal='+str(sinusoidal)+'_D='\
                +str(propDistance)+'_microns.pdf')

    plt.clf()
