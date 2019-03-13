from All_Fun import *

# For definiteness, use λ = 500nm, d=100 microns,
# D = 1.0m and L =5mm. Overlay on your plot the #
#theoretical value of the intensity pattern expected
FFT_Intensity(slitWidth=100, x_lim=200, AppertureWidth=100000,\
             propDistance=5*10**3,  wavelength=0.5,Task=1, bins=2048*2**3)

#Now calculate and plot the Fraunhofer diffraction pattern of a sinusoidal phase grating.
#This grating is a slit of extent d = 2mm, outside of which the transmission is zero.
#Within |x| < d/2, the transmission amplitude is 1.0, and the phase of A is
#φ(x) = (m/2) sin(2πx/s)
#where s is the spacing of the phase maxima, and can be taken as 100microns for this problem.
#For this calculation, use m = 8. The Fresnel distance d2/λ is 8 m, so calculate
# the pattern on a screen at D = 10 m. What do you notice about the resulting pattern?
FFT_Intensity(Task=2, sinusoidal=True, plt_theory=False, m=8, s=100,\
              slitWidth=2000,  propDistance=10*10**6)

#Now modify your program so that the calculation is accurate even in
#the near-field by adding a phase correction to the aperture function
# as defined by Equation 9. Repeat your calculations in the previous#
# two tasks for D = 5mm for the slit, and D = 0.5m for the phase grating,
#and plot the results. Do the intensity patterns look sensible?

FFT_Intensity(Task=3,slitWidth=100, x_lim=200, plt_theory=False, AppertureWidth=10000,\
              propDistance=5*10**3,  wavelength=0.5, bins=2048*2**3)
FFT_Intensity(Task=3, sinusoidal=True, plt_theory=False, m=8, s=100,\
              slitWidth=1000,  propDistance=0.5*10**6, x_lim = 800)

#for i in [500*x for x in range(1,40)]:
#    FFT_Intensity(slitWidth=i, Task=3)
