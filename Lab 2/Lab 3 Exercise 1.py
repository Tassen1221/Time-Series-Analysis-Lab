import numpy as np
import matplotlib.pyplot as plt

def Gaussian(t,h):
    return (1/(np.sqrt(np.pi)*h))*np.exp(-(t/h)**2)

def Fourier(w,h):
    return np.exp(-((w**2)*(h**2))/4)

x = np.arange(-100,100,0.001)
plt.plot(x,Gaussian(x,20), label = "20s Half-Duration")
plt.plot(x,Gaussian(x,40), label = "40s Half-Duration")
plt.xlabel("Time (s)")
plt.ylabel("Probability Density (1/s)")
plt.title("Gaussian Distribution with 20s and 40s Half-Durations")
plt.legend()
plt.show()

g1 = Gaussian(x,20)
A = np.fft.fft(g1)*0.001
A = np.fft.fftshift(A)
f_axis1 = np.fft.fftshift(np.fft.fftfreq(len(g1), 0.001) )
w_axis1 = 2*np.pi*f_axis1

g2 = Gaussian(x,40)
B = np.fft.fft(g2)*0.001
B = np.fft.fftshift(B)
f_axis2 = np.fft.fftshift(np.fft.fftfreq(len(g2),0.001))
w_axis2= 2*np.pi*f_axis2

C = Fourier(x,20)
D = Fourier(x,40)

plt.plot(w_axis1,np.abs(A), label = "DFT of Gaussian with 20s Half-Duration")
plt.plot(x,C, label = "Analytical FT of Gaussian with 20s Half-Duration")
plt.plot(w_axis2,np.abs(B), label = "DFT of Gaussian with 40s Half-Duration")
plt.plot(x,D, label = "Analytical FT of Gaussian with 20s Half-Duration")
plt.xlim(-0.5,0.5)
plt.xlabel("Angular Frequency (rad/s)")
plt.ylabel("Amplitude (1/s)")
plt.title("Fourier Transforms of Gaussian Distribution with 20s and 40s Half-Durations")
plt.legend()
plt.show()