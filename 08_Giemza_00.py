
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time
dt = 24*60*60*2
t = 0
i = 0
n = 3
G = 6.673*10**-11
ms = 2.*10**30
mz = 6.*10**24
mm = 6.4*10**23

m = np.array([[ms],
              [mz],
              [mm]])

R = np.array([[0.,0.,0.],
              [149598023*1000.,0.,0.],
              [227939200*1000.,0.,0.]])

V = np.array([[0.,0.,0.],
              [0.,2*np.pi*149598023*1000./(365*24*60*60),0.],
              [0.,2*np.pi*227939200*1000./(686.971*24*60*60),0.]])


def accel(R):
    A = np.zeros([n,3])
    for i in range(n):
        for j in range(n):
            if i != j:
                #print(i, j)
                rij = np.sum((R[i, :] - R[j, :]) * (R[i, :] - R[j, :])) ** 0.5
                dir = R[j, :]  - R[i, :]
                A[i, :] += G*m[j,0]/(rij**3)*dir
    return A

accel(R)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

wframe = None
minbound = -1.3 * np.max(R)
maxbound = 1.3 * np.max(R)

while True:
    A = accel(R)
    dV = A*dt
    V += dV
    dR = V*dt
    R += dR
    t += dt
    i += 1

    
    
 

    if wframe:
        ax.collections.remove(wframe)
    
    wframe = ax.scatter(R[:, 0], R[:, 1], R[:, 2], c = ['r', 'g', 'b'], label = str(t/24*60*60))

    ax.legend()
    
    ax.auto_scale_xyz([minbound, maxbound], [minbound, maxbound], [minbound, maxbound])
    
    plt.pause(.0001)