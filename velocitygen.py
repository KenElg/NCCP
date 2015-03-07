# velocitygen.py --- Generates particle velocities V
import numpy as np
from cdf import MB_ICDF
from scipy.interpolate import interp1d as interp
def velgen(n,T,L):
    rand_nums = np.random.random(n)
    icdf = MB_ICDF(T,L)
    Vmag = icdf(rand_nums)
# Spherical polar coords - generate random angle for velocity vector, uniformly distributed over the surface of a sphere
    theta = np.arccos(np.random.uniform(-1,1,n))
    phi = np.random.uniform(0,2*np.pi,n)
    v = np.array([np.sin(theta)*np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)])
    # convert to cartesian units
    V = np.transpose(Vmag*v)
    return V
