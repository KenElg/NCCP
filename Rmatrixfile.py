# Rmatrixfile.py --- Here we have a function that creates our initial R and V matrices for dens and T
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import erf
from scipy.interpolate import interp1d as interp
from cdf import MB_ICDF
from velocitygen import velgen
def init_matrix(dens,T):
    rows=3
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
    V = velgen(n,T,L)
    return R,V,L,n
