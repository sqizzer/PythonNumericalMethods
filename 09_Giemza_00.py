from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import constants as const 
n = 3
k = 9E9
e = 1.6E-19

me = 9.1E-31
mp = 1.67E-27
mn = 1.67E-27
mj = 2*me + 2*mn
r = const.epsilon_0*const.h**2/(2*const.pi*const.elementary_charge**2*const.electron_mass)
v = const.elementary_charge**2/(const.epsilon_0*const.h)

T = 2.93e-27

#___________________________________________________________________________

m = np.array([[mj],
          [me],
          [me]])

R = np.array([[0,0.,0.],
              [r,0.,0.],
              [-r,0.,0.]])

v = np.array([[0.,0,0.],
              [0,v,0.],
              [0,-v,0.]])

q = np.array([[e],
	[-e],
	[-e]])

#___________________________________________________________________________

def accel(R):
	a = np.zeros([n, 3])
	
	for i in range(n):
		for j in range(n):
			if i != j:
				
				
				
				rij = np.sum((R[i, :] - R[j, :]) * (R[i, :] - R[j, :])) ** 0.5		
				dir = R[j, :] - R[i, :]		
				a[i, :] += -k * q[i, 0] * q[j, 0]/(m[i, 0] * rij ** 3) * dir		
														
	return a

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")


wframe = None

#___________________________________________________________________________

i, t = 0, 0.0
dt = 100000000 * T

minbound = -1 * np.max(R)
maxbound = 1 * np.max(R)

while True:
	a = accel(R)
	dv = a * dt		
	v += dv		
	dR = v * dt		
	R += dR		
	t += dt
	i += 1
	
	if wframe:
		ax.collections.remove(wframe)		# checks if frame is generated; if yes, it is deleted

	wframe = ax.scatter(R[:, 0], R[:, 1], R[:, 2], c = ["r", "b", "b"], label = str(t))		# scatter - points are generated

	ax.legend()
	ax.auto_scale_xyz([minbound, maxbound], [minbound, maxbound], [minbound, maxbound])
	plt.pause(.0001)