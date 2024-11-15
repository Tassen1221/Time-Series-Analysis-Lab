import numpy as np
import matplotlib.pyplot as plt

def myConv(f,w):
    g = [0]*(len(f)+len(w)-1)
    for n in range(len(f)+len(w)-1):

        for k in range(len(w)):
            if n-k < 0 or n-k >= len(f):
                g[n] += 0
            else:
                g[n] += f[n-k]*w[k]
    return g

f = np.random.rand(50)
w = np.random.rand(100)

x = np.arange(0,149)
y = myConv(f,w)-np.convolve(f,w)

plt.plot(x,y)
plt.xlabel("Index of g")
plt.ylabel("Difference between myConv and Numpy Convolution")
plt.title("Residual of myConv and Numpy Convolution for f and w")
plt.show()

import time
times = []*4
i = 10
while i <= 10000:
    f = np.random.rand(i)
    w = np.random.rand(i)
    t1 = time.time()
    g = myConv(f, w)
    t2 = time.time()
    g = np.convolve(f,w)
    t3 = time.time()
    times.append((t2-t1)-(t3-t2))
    i*=10

x = [10,100,1000,10000]
y = times

plt.plot(x,y)
plt.xlabel("Size of Arrays Convolved")
plt.ylabel("Time Difference between myConv and\nNumpy Convolution (seconds)")
plt.title("Time Difference between myConv and Numpy Convolution vs Size of Convolved Arrays")
plt.show()