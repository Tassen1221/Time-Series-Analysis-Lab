import numpy as np
import matplotlib.pyplot as plt

def ratFilter(N,D,x):
    Nx = N[0]+N[1]*x+N[2]*(x**2)
    Dx = D[0]+D[1]*x+D[2]*(x**2)
    return Nx/Dx

x = np.linspace(0,100,1200)
z = np.zeros(1200)
z[0] = (1/12)
z = np.exp(-1j*z*(1/12))
e = 0.05
N = [1/(1+e),(-1/(1+e))*(np.exp(-1j*np.pi/2)+np.exp(-1j*np.pi/6)),(1/(1+e))*np.exp(-np.pi/3)]
D = [1,(-1/(1+e))*(np.exp(-1j*np.pi/2)+np.exp(-1j*np.pi/6)),(1/(1+e)**2)*np.exp(-np.pi/3)]

plt.plot(x,ratFilter(N,D,z))
plt.xlabel("Frequency (1/Year)")
plt.ylabel("Amplitude (Unitless)")
plt.title("Notch Filter Impluse Response for dt = (1/12) Years")
plt.xlim(0,6)
plt.show()

F = np.zeros(1200)
for i in range(len(x)):
    F[i] = np.abs(np.sum(ratFilter(N,D,z)*np.exp(-1j*x[i]*i*(1/12))))

plt.plot(x,np.fft.fft(ratFilter(N,D,z)), label = "FFT")
plt.plot(x,F, label = "Spectrum Amplitude")
plt.xlabel("Frequency (1/Year)")
plt.ylabel("Amplitude (Unitless)")
plt.title("Notch Filter Impluse Response FFT and Theoretical Spectrum Amplitude")
plt.legend()
plt.xlim(0,6)
plt.show()



