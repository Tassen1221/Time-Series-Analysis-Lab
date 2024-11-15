import numpy as np
import matplotlib.pyplot as plt

def W(M,z,f0,fs,e):
    q1 = np.exp(-1j*2*np.pi*(f0)/(fs))
    q2 = np.exp(1j*2*np.pi*(f0)/(fs))
    p1 = (1+e)*q1
    p2 = (1+e)*q2
    return M*((z-q1)/(z-p1))*((z-q2)/(z-p2))

M = 1.05
f0 = 1
fs = 12
e = 0.05

w = np.linspace(-fs/2,fs/2,1000)
z = np.exp(-1j*w*(1/12))

plt.plot(w, np.abs(W(M,z,f0,fs,e)**2))
plt.xlabel("Frequency (1/Year)")
plt.ylabel("Amplitude (Unitless)")
plt.title("Notch Filter Z-Transform Frequency vs Amplitude")
plt.show()
    
for i in range(len(np.abs(W(M,z,f0,fs,e)**2))):
    if np.abs(W(M,z,f0,fs,e)**2)[i] > 0.5*np.abs(W(M,z,f0,fs,e)**2)[499]:
        print(np.abs(2*w[i]))
        break
