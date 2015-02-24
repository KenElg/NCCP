# Main File
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
pi=math.pi

dens=0.8
T=2

from Rmatrixfile import init_matrix
R,V=init_matrix(dens,T) # Here we plot our R matrix as a scatter plot    
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