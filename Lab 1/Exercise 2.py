import numpy as np
import matplotlib.pyplot as plt

def RLresponse(R,L,V_in,dt):
    r = [0]*len(V_in)
    for t in range(len(V_in)):
        if t == 0:
            r[t] = (1/dt)-(R/L)*np.exp(-R*t*dt/L)*(0.5)
        else:
            r[t] = -(R/L)*np.exp(-R*t*dt/L)
    return np.convolve(r,V_in)*dt

def step(R,L,V_in,dt):
    s = [0]*len(V_in)
    for t in range(len(V_in)):
        if t == 0:
            s[t] = 0.5*np.exp(-R*t*dt/L)
        else:
            s[t] = np.exp(-R*t*dt/L)
    return s
V_in = [0.5]+[1]*99
t = np.linspace(0,0.03,199)
t2 = np.linspace(0,0.015,100)
plt.plot(t2,step(950,4,V_in,0.00015), color = "orange", label = "Step Response Function")
plt.plot(t2,RLresponse(950,4,V_in,0.00015)[0:100], ls = "", marker = "o", ms = 2, mec = "blue", label = "Convolution of Impulse Response and Heaviside Input")
plt.legend()
plt.xlabel("Time (Seconds)")
plt.ylabel("Voltage (Volts)")
plt.title("Comparison of Step Function and Convolution for RL Circuit")
plt.show()

def impluse(R,L,V_in,dt):
    i = [0]*len(V_in)
    for t in range(len(V_in)):
        if t == 0:
            i[t] = (1/dt)-(R/L)*np.exp(-R*t*dt/L)*(0.5)
        else:
            i[t] = -(R/L)*np.exp(-R*t*dt/L)
    return i
V_in = [1/0.00015]+[0]*99
t = np.linspace(0,0.03,199)
t2 = np.linspace(0,0.015,100)
plt.plot(t2[0:100],impluse(950,4,V_in,0.00015)[0:100], color = "orange", label = "Impulse Response Function")
plt.plot(t2[0:100],RLresponse(950,4,V_in,0.00015)[0:100], ls = "", marker = "o", ms = 2, mec = "blue", label = "Convolution of Impulse Response and Delta Input")
plt.legend()
plt.xlabel("Time (Seconds)")
plt.ylabel("Voltage (Volts)")
plt.title("Comparison of Impluse Function and Convolution for RL Circuit")
plt.show()

