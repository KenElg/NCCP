# Main File
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
pi=math.pi

dens=0.8
T=1

from Rmatrixfile import init_matrix
R,V,L,n=init_matrix(dens,T) # Here we make our initial matrices
#Here we plot the initial R matrix     
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R[:,0], R[:,1], R[:,2], c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# next is the force function

# next is the movement

# next is the pressure