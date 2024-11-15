import numpy as np
import matplotlib.pyplot as plt

file  = open("methane_global.csv",'r')
CH4 = file.read()
CH4 = CH4.split(',')

date = CH4[8:len(CH4):6]
date = [float(i) for i in date]

average = CH4[9:len(CH4):6]
average = [float(i) for i in average]

trendfit = np.polyfit(date,average,1)
trend = []
for i in range(len(date)):
    trend.append(date[i]*trendfit[0]+trendfit[1])

newaverage = []
for i in range(len(average)):
    newaverage.append(average[i]-trend[i])
plt.plot(date,average, label = "Global Methane Average")
plt.plot(date,trend, label = "Global Methane Average Trend")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average and Trend")
plt.legend()
plt.show()


plt.plot(date,newaverage, label = "Global Methane Average Detrended")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average Detrended")
plt.legend()
plt.show()

newaverage = np.array(newaverage)
z = np.exp(-1j*newaverage*(1/12))

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

plt.plot(date,W(M,z,f0,fs,e)+trend, label = "Global Methane Average Detrended and Filtered")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average Detrended and Filtered")
plt.legend()
plt.show()

fftnewaverage = np.fft.fft(newaverage)
length = len(date)
freq = np.fft.fftfreq(length, d=(1/12))
plt.plot(freq,np.real(fftnewaverage), label = "FFT Amplitude")
plt.plot(freq,np.imag(fftnewaverage), label = "FFT Phase")
plt.xlabel("Frequency (1/Year)")
plt.ylabel("Amplitude (Unitless)")
plt.title("FFT Amplitude and Phase of Detrended Global Methane Average")
plt.legend() 
plt.show()

for i in range(len(freq)):
    if freq[i] < -0.9:
        fftnewaverage[i] = 0
    if freq[i] > 0.9:
        fftnewaverage[i] = 0

plt.plot(freq,np.real(fftnewaverage), label = "FFT Amplitude")
plt.plot(freq,np.imag(fftnewaverage), label = "FFT Phase")
plt.xlabel("Frequency (1/Year)")
plt.ylabel("Amplitude (Unitless)")
plt.title("FFT Amplitude and Phase of Detrended Global Methane Average")
plt.legend() 
plt.xlim(0,2.5)
plt.show()

ifftnewaverage = np.fft.ifft(fftnewaverage)

plt.plot(date,ifftnewaverage+trend, label = "Global Methane Average Detrended and FFT Filtered")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average Detrended and FFT Filtered")
plt.legend() 
plt.show()

plt.plot(date,average, label = "Global Methane Average")
plt.plot(date,W(M,z,f0,fs,e)+trend, label = "Global Methane Average Detrended and Filtered")
plt.plot(date,ifftnewaverage+trend, label = "Global Methane Average Detrended and FFT Filtered")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average Detrended and FFT Filtered")
plt.legend() 
plt.show()

average = np.array(average)
z = np.exp(-1j*average*(1/12))

fftaverage = np.fft.fft(average)
length = len(date)
freq = np.fft.fftfreq(length, d=(1/12))

for i in range(len(freq)):
    if freq[i] < -0.9:
        fftnewaverage[i] = 0
    if freq[i] > 0.9:
        fftnewaverage[i] = 0

ifftaverage = np.fft.ifft(fftaverage)

plt.plot(date,average, label = "Global Methane Average")
plt.plot(date,W(M,z,f0,fs,e), label = "Global Methane Average Filtered")
plt.plot(date,ifftaverage, label = "Global Methane Average FFT Filtered")
plt.xlabel("Year")
plt.ylabel("Methane Average (Parts Per Billion)")
plt.title("Yearly Global Methane Average FFT Filtered")
plt.legend() 
plt.show()