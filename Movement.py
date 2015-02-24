# Change R and V matrices with time
# R matrix
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
dt=0.001
R=R+V*dt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R[:,0], R[:,1], R[:,2], c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# V matrix 
V[:,1]=V[:,1]+fx*dt
V[:,2]=V[:,2]+fy*dt
V[:,3]=V[:,3]+fz*dt