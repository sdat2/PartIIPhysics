import numpy as np
import matplotlib.pyplot as plt
dt=0.01
fftsize=256
t=np.arange(fftsize)*dt
#Generate some fake data at 12 Hz and 34 Hz
y=np.cos(2*np.pi*12*t)+0.5*np.sin(2*np.pi*34*t)
plt.plot(t,y)
plt.savefig('Ex_Signal.pdf')
plt.clf()

Y=np.fft.fft(y)
# Plot FFT modulus versus array index
plt.subplot(2,1,1); plt.plot(abs(Y))
# Now use the correct frequency coordinates
f=np.fft.fftfreq(fftsize,dt)
plt.subplot(2,1,2); plt.plot(f,abs(Y))
plt.savefig('Ex_2sided.pdf')
plt.clf()

plt.subplot(2,1,1); plt.plot(f,Y.real)
plt.subplot(2,1,2); plt.plot(f,Y.imag)
plt.savefig('Ex_withnegatives.pdf')
plt.clf()

Y2=np.fft.fftshift(Y)
f2=np.fft.fftshift(f)
plt.subplot(2,1,1); plt.plot(f2,Y2.real)
plt.subplot(2,1,2); plt.plot(f2,Y2.imag)
plt.savefig('Ex_withoutnegatives.pdf')
plt.clf()
