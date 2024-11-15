import numpy as np
import matplotlib.pyplot as plt

file = open("RAYN.II.LHZ.sem", "r")

time = []
displacement = []
for i in file.readlines():
    if float(i.split()[0]) >=0 and float(i.split()[0]) <= 800:
        time.append(float(i.split()[0]))
        displacement.append(float(i.split()[1]))


plt.plot(time,displacement)
plt.xlabel("Time (Seconds)")
plt.ylabel("Vertical Displacement (Meters)")
plt.title("RAYN Station Raw Vertical Synthetic Seismogram")
plt.show()


def Gaussian(t, th):
    g = []
    for i in t:
        g.append((1/(np.sqrt(np.pi)*th))*np.exp(-(i/th)**2))
    return g

Gaussiantime1 = np.arange(-30,30,0.1615)
Gaussiantime2 = np.arange(-60,60,0.1615)
plt.plot(Gaussiantime1,Gaussian(Gaussiantime1,10), label = "10s Half-Duration")
plt.plot(Gaussiantime2,Gaussian(Gaussiantime2,20), label = "20s Half-Duration")
plt.xlabel("Time (Seconds)")
plt.ylabel("Y-Value (Unitless)")
plt.title("Gaussian Distributions for 10s and 20s Half-Duration\nfrom -3 x Half-Duration to 3 x Half-Duration")
plt.legend()
plt.show()

convolution1 = list(np.convolve(displacement,Gaussian(time,10)))
convolution2 = list(np.convolve(displacement,Gaussian(time,20)))
plt.plot(time,convolution1[0:4954], label="10s Half-Duration Convolution")
plt.plot(time,convolution2[0:4954], label="20s Half-Duration Convolution")
plt.plot(time,displacement, label="Raw Timeseries")
plt.xlabel("Time (Seconds)")
plt.ylabel("Vertical Displacement (Meters)")
plt.title("Comparison of Convolution with Gaussians and Raw Timeseries\nof RAYN Station Raw Vertical Synthetic Seismogram")
plt.legend()
plt.show()
