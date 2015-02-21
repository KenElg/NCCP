import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pi=math.pi
# Here we have a function that creates our initial R and V matrices for dens and T
def init_matrix(dens,T):
    rows=6
    i=0
    n=4*rows**3
    vol=n/dens
    L=vol**(1.0/3)
    R=np.zeros((n,3),dtype=float)
    for x in range(0,rows):
        for y in range(0,rows):
            for z in range (0,rows):
                R[i:i+4,:]=np.array([[0+x,0+y,0+z],[0.5+x,0.5+y,0+z],[0.5+x,0+y,0.5+z],[0+x,0.5+y,0.5+z]]) 
                i=i+4
    R=R*L/rows
    vs=T*0.5
    V=np.random.normal(0,vs,(n,3))
    print (R)
    return R,V
#    raw_input()

#R,V=init_matrix(0.8,1) # Here we plot our R matrix as a scatter plot    
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(R[:,0], R[:,1], R[:,2], c='b', marker='o')
#
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

#plt.show()
