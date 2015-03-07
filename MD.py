# MD.py --- Runs simulation
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from forcetestken import force
from Rmatrixfile import init_matrix
from update import update_func
from josplot import AnimatedScatter
from pot import pot
rho_c = 3.2
dens = 0.8
T = 1
R,V,L,n = init_matrix(dens,T)
dt = 0.004
tf = np.zeros((n,3))
a = AnimatedScatter(n, L, R, V, update_func, dt, tf, T)
a.show()

