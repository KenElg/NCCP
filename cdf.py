# cdf.py  --- Cumulative Maxwell-Boltzmann 
#distribution function and its inverse
import numpy as np
from scipy.special import erf
from scipy.interpolate import interp1d as interp
def MB_ICDF(T,L):
#    Cumulative Distribution function of the 
#    Maxwell-Boltzmann speed distribution
    a = np.sqrt(T)
    v = np.arange(0,L,0.1)
    cdf = erf(v/(np.sqrt(2)*a)) - np.sqrt(2/np.pi)* v* np.exp(-v**2/(2*a**2))/a
    icdf = interp(cdf,v)
    return icdf
