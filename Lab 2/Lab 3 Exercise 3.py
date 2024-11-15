import numpy as np
import matplotlib.pyplot as plt

from argon import YanData, dk, massRho, molWeight, Navogadro

Data = list(YanData[:0:-1]) + list(YanData)
x = np.arange(-len(YanData)*dk,len(YanData)*dk,dk)[1::]

Result = []

for i in range(len(Data)):
    Result += [(1j/np.pi)*x[i]*(Data[i]-1)]

plt.plot(x,np.imag(Result))
plt.xlabel("Wavenumber (1/A)")
plt.ylabel("P(k) (Imaginary)")
plt.title("Fourier Transform of p(r) from -10(1/A) to 10(1/A)")
plt.xlim(-10,10)
plt.show()

rho = (massRho/molWeight)*Navogadro*10**(-24)

def RDF(S,dk,rho,r):
    k = np.arange(0,len(S)*dk,dk)
    return 1 + (1/2*np.pi**2*r)*dk*sum(k*(S-1)*np.sin(k*r))

def RDFcalc(S,dk,rho):
    Result = []
    for i in range(1,21):
        Result.append(RDF(S,dk,rho,i))
    return [Result,list(np.arange(1,21))]

plt.plot(RDFcalc(YanData,dk,rho)[1],RDFcalc(YanData,dk,rho)[0])
plt.xlabel("Distance (A)")
plt.ylabel("Relative Probability (Unitless)")
plt.title("Radial Distribution Function of Argon from 0 to 20 Angstroms")
plt.show()

YanDataOld = YanData

while len(YanData) > 1:
    plt.plot(RDFcalc(YanData,dk,rho)[1],RDFcalc(YanData,dk,rho)[0], label = "Kmax ="+str(len(YanData)*dk))
    YanData = YanData[0:len(YanData)//2]
plt.xlabel("Distance (A)")
plt.ylabel("Relative Probability (Unitless)")
plt.title("Radial Distribution Function of Argon from 0 to 20 Angstroms")
plt.legend()
plt.show()

YanData = YanDataOld

while dk < 8:
    plt.plot(RDFcalc(YanData,dk,rho)[1],RDFcalc(YanData,dk,rho)[0], label = "Dk ="+str(dk))
    dk = dk*2
    YanData = YanData[0:-1:2]
plt.xlabel("Distance (A)")
plt.ylabel("Relative Probability (Unitless)")
plt.title("Radial Distribution Function of Argon from 0 to 20 Angstroms")
plt.legend()
plt.show()

