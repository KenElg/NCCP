# Made by Craig Finch van shocksolution.com
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from forcetestken import force
from Rmatrixfile import init_matrix
from update import update_func
from josplot import AnimatedScatter
from pot import pot
from paircorr3D import PairCorrelationFunction_3D
rho_c = 3.2
dens = 0.8
T = 1
R,V,L,n = init_matrix(dens,T)
dt = 0.004
tf = np.zeros((n,3))
nsteps=0
for i in range(0,nsteps):
    R,V=update_func(n,L,R,V,dt,tf,T)
x=R[:,0]
y=R[:,1]
z=R[:,2]
rMax=0.32*L
dr=0.02
g, radii, interior_x, interior_y, interior_z= PairCorrelationFunction_3D(x,y,z,L,rMax,dr)
fig = plt.figure()
plt.plot(radii,g)
plt.title('g(r) after %d time steps' % nsteps)
plt.xlabel('r')
plt.ylabel('g(r)')
plt.show()
#fig.figsave('g_1000.png')
