import numpy as np
import matplotlib.pyplot as plt

tmp = np.genfromtxt("nwao.vh1")
nwao = tmp.flatten()

time = nwao[0:len(nwao):2]
data = nwao[1:len(nwao):2]

plt.plot(time/3600, data)
plt.xlabel("Time (Hours)")
plt.ylabel("Velocity")
plt.title("Time vs Velocity Seismic Data from Narrogin, Western Australia")
plt.show()

p = (np.abs(np.fft.fft(data))**2)/time
w = 1000*np.fft.fftfreq(len(data),10)
arg = np.argsort(w)
p = p[arg]
w = w[arg]

w1 = w
p1 = p

plt.plot(w, p)
plt.xlabel("Frequency (mHz)")
plt.ylabel("Amplitude")
plt.title("Frequency vs Amplitude Seismic Data from Narrogin, Western Australia")
plt.show()

trendfit = np.polyfit(time,data,1)
trend = []
for i in range(len(data)):
    trend.append(w[i]*trendfit[0]+trendfit[1])

data = data-trend
n = np.arange(0,len(data))

hann = 1-np.cos(2*np.pi*n/len(data))
data = data*hann

p = (np.abs(np.fft.fft(data))**2)/time
w = 1000*np.fft.fftfreq(len(data),10)
arg = np.argsort(w)
p = p[arg]
w = w[arg]

plt.plot(w, p)
plt.xlabel("Frequency (mHz)")
plt.ylabel("Amplitude")
plt.title("Frequency vs Amplitude Detrended Seismic Data\nwith Hann Window from Narrogin, Western Australia")
plt.show()

plt.plot(w1,p1,label = "Original Data")
plt.plot(w,p,label = "Detrended and Hann Window Data")
plt.xlim(0.1,2.6)
plt.xlabel("Frequency (mHz)")
plt.ylabel("Amplitude")
plt.title("Frequency vs Amplitude Seismic Data\nfrom Narrogin, Western Australia Compared")
plt.legend()
plt.show()

plt.plot(w1,p1,label = "Original Data")
plt.plot(w,p,label = "Detrended and Hann Window Data")
plt.annotate("2S3",[1.244,2.877*10**12],[1.3,2.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("1S5",[1.365,1.1*10**11],[1.25,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("2S4",[1.385,1.1*10**11],[1.4,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("0T9",[1.495,1.1*10**11],[1.55,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("0S9",[1.584,1.1*10**11],[1.7,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("1S0",[1.625,1.1*10**11],[1.85,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("0S14",[2.224,1.1*10**11],[2,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.annotate("0S16",[2.456,1.1*10**11],[2.2,0.7*10**12], arrowprops=dict(arrowstyle = "->"))
plt.xlim(0.1,2.6)
plt.xlabel("Frequency (mHz)")
plt.ylabel("Amplitude")
plt.title("Frequency vs Amplitude Seismic Data\nfrom Narrogin, Western Australia Compared with Modes")
plt.legend()
plt.show()