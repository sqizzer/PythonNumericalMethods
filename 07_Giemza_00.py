from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import minimize
X = []
e = 1.
s = 1.
n = 10
i=1
j=1
R = np.random.rand(3*n)

"""
r13 = np.sqrt((x[0]-x[2])**2+(y[0]-y[2])**2+(z[0]-z[2])**2)
r23 = np.sqrt((x[1]-x[2])**2+(y[1]-y[2])**2+(z[1]-z[2])**2)
r12 = np.sqrt((x[0]-x[1])**2+(y[0]-y[1])**2+(z[0]-z[1])**2)
V13 = 4*eps*((sig/r13)**12-(sig/r13)**6)
V23 = 4*eps*((sig/r23)**12-(sig/r23)**6)
V12 = 4*eps*((sig/r12)**12-(sig/r12)**6)



#Vij = 4*eps*((sig/rij)**12-(sig/rij)**6)
#R1 = np.array([[x1,y1,z1],[x2,y2,z2],[x3,z3,y3]])"""




"""def V(R):
    
    V = 0
    R = R.reshape(n, 3)
    
    
 
    for i in range(n):
        for j in range(i+1, n):
            rij = np.sum((R[i,:]-R[j,:])*(R[i,:]-R[j,:]))**0.5
            
            V += 4*e*((s/rij)**12-(s/rij)**6)  
                         
    return V 
      
    
print(V(R))
x0 = minimize(V, R, method = 'Nelder-Mead')
#print(x0)
#R = r0.reshape(n, 3)




def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin"""




def r_ij(xi, yi, zi, xj, yj, zj):
    return np.sqrt((xi-xj)**2+(yi-yj)**2+(zi-zj)**2)

def V_ij(xi, yi, zi, xj, yj, zj):
    return 4 * e * ((s/r_ij(xi, yi, zi, xj, yj, zj))**12 - (s/r_ij(xi, yi, zi, xj, yj, zj))**6)


def V(R):
    
    V = 0
    R = R.reshape(n, 3)
    
    
 
    for i in range(n):
        for j in range(i+1, n):
            rij = np.sum((R[i,:]-R[j,:])*(R[i,:]-R[j,:]))**0.5
            
            V += 4*e*((s/rij)**12-(s/rij)**6)  
                         
    return V   


print("potencjał wynosi :",V(R))

res = minimize(V, R, method='Nelder-Mead',tol=1e-6)
data = res.x.reshape(n,3)

print("wartosci funckji wynosza: ",data)


fig = plt.figure()
ax = plt.axes(projection='3d')

R = R.reshape(n,3)
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('Z ')
ax.scatter3D(data[:,0],data[:,1],data[:,2],cmap='Reds')
ax.scatter3D(R[:,0],R[:,1],R[:,2],cmap='Blues')


plt.show()




    


    
    

