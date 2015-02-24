import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
dens=3E10
T=300
pi=(math.pi)
rows=6
i=0
n=4*rows**3
vol=n/dens
L=vol**(1/3)
R=np.zeros((n,3),dtype=float)
Rf=np.zeros((n,3),dtype=float)
for x in range(0,rows):
    for y in range(0,rows):
        for z in range (0,rows):
            R[i:i+4,:]=np.array([[0+x,0+y,0+z],[0.5+x,0.5+y,0+z],[0.5+x,0+y,0.5+z],[0+x,0.5+y,0.5+z]]) 
            i=i+4
    vs=T*0.5
    V=np.random.normal(0,vs,(n,3))

Rf=R*L/rows
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Rf[:,0], Rf[:,1], Rf[:,2], c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
