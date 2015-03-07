# update.py --- updates R,V after every iter
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from forcetestken import force

def update_func(n,L,R,V,dt,tf,T):
    tf=force(R,tf,L,[n]) 
    target=T
    R=(R+V*dt)%L
    V+=tf*dt
    avV=np.sum(V**2)/n
    temp=1/3.0*avV
    lada=math.sqrt(target/temp)
    V=lada*V
    return R,V

