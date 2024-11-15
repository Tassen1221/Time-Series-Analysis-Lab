import numpy as np
import matplotlib.pyplot as plt

def Boxcar(t,T):
    result = []
    for i in t:
        if i >= 0 and i <= T:
            result.append(1)
        else:
            result.append(0)
    return result

def Hann(t,T):
    result = []
    for i in t:
        if i >= 0 and i <= T:
            result.append(0.5*(1-np.cos(2*np.pi*i/T)))
        else:
            result.append(0)
    return result

t = np.arange(-100,100,0.01)

plt.plot(t,Boxcar(t,10), label = "Boxcar")
plt.plot(t,Hann(t,10), label = "Hann Window")
plt.xlim(-5,15)
plt.xlabel("Time (s)")
plt.ylabel("Y-Axis (Unitless)")
plt.title("Boxcar and Hann Window Functions for T of 10s")
plt.legend()
plt.show()


A = np.fft.fft(Boxcar(t,10))*0.01
A = np.fft.fftshift(A)
f_axis1 = np.fft.fftshift(np.fft.fftfreq(len(A), 0.01))
w_axis1 = 2*np.pi*f_axis1

B = np.fft.fft(Hann(t,10))*0.01
B = np.fft.fftshift(B)
f_axis2 = np.fft.fftshift(np.fft.fftfreq(len(B), 0.01))
w_axis2 = 2*np.pi*f_axis2

plt.plot(w_axis1,np.abs(A), label = "Boxcar")
plt.plot(w_axis2,np.abs(B), label = "Hann Window")

plt.xlim(-10,10)
plt.xlabel("Angular Frequency (rad/s)")
plt.ylabel("Amplitude (Unitless)")
plt.title("Fourier Transforms of Boxcar and Hann Window Functions for T of 10s")
plt.legend()
plt.show()