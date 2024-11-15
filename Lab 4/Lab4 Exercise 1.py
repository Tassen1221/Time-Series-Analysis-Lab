import numpy as np
import matplotlib.pyplot as plt

tmp = np.genfromtxt("PHL_data.txt")
phl = tmp.flatten()

tmp = np.genfromtxt("MLAC_data.txt")
mlac = tmp.flatten()

zeros = np.zeros(250)

mlac = np.concatenate((zeros,mlac,zeros))

answer = [0]*501
for i in range(501):
    answer[i] = sum(np.conjugate(np.fft.fft(mlac[i:86400+i]))*np.fft.fft(phl))

plt.plot(np.arange(-250,251),answer)
plt.xlabel("Time Delay (s)")
plt.ylabel("Amplitude")
plt.title("Amplitude for Time Delay from -250s to 250s\nof Cross-Correlation of Seismogram Data")
plt.show()

phl = np.sign(phl)
mlac = np.sign(mlac)

answer = [0]*501
for i in range(501):
    answer[i] = sum(np.conjugate(np.fft.fft(mlac[i:86400+i]))*np.fft.fft(phl))

plt.plot(np.arange(-250,251),answer)
plt.xlabel("Time Delay (s)")
plt.ylabel("Amplitude")
plt.title("Bit Conversion Amplitude for Time Delay from -250s to 250s\nof Cross-Correlation of Seismogram Data")
plt.show()