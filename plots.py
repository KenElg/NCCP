import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from forcetestken import force
from Rmatrixfile import init_matrix
from update import update_func
from josplot import AnimatedScatter
from pot import pot
from paircorr3D import PairCorrelationFunction_3D # Written by Craig Finch of shocksolution.com
from pressure import pressure
rho_c = 3.2
dens = 0.8
T = 1
R,V,L,n = init_matrix(dens,T)
dt = 0.004
tf = np.zeros((n,3))
nsteps=1000
cv=np.zeros((1,nsteps))
cv_error=np.zeros((1,nsteps))
P = np.zeros((1,nsteps))
U=np.zeros((1,nsteps))
v = np.zeros(nsteps)
ET = np.zeros(nsteps)
t=np.zeros((1,nsteps))
t[0,:]=np.arange(0,nsteps*dt,dt)
f =0
p=np.zeros((nsteps))
def calc_Cv(n,L,R,V,dt,tf,T,cv,error):
    Ekin=0.5*V**2
    delta=np.std(Ekin**2)
    Exp=np.mean(Ekin**2)
    X=delta/Exp
    cv_error[0,i]=np.var(Ekin)/math.sqrt(n)
    cv[0,i]=(3.0/2)*n*(1/(1-(3.0*n/2)*X))
    return cv,cv_error
    
def press_calc(R,V,n,rho_c):
    S =  0
    dr = np.zeros((1,3))
    for j in range(0,n):
        for x in range(1,j-1):              
            dr[:] = np.subtract(R[x,:], R[j,:])          
            dr = dr - L * np.rint(dr/L)              
            rho = np.sum(dr**2)         
            
            if (rho < rho_c**2):      
                dU = (48*rho**(-7) - 24*rho**(-4))     
                f = -dU * dr
                S = S + np.sum(dr*f) 
         
    P[0,i] = dens/(3*n)  *(np.sum(V**2) + S)
    return P



    
for i in range(0,nsteps):
    R,V=update_func(n,L,R,V,dt,tf,T)   
    cv,cv_error=calc_Cv(n,L,R,V,dt,tf,T,cv,cv_error)
    P = press_calc(R,V,n,rho_c)
    U = pot(R,L,U,n)
    v = 0.5 * np.sum(V**2) 
    ET[i]= v + U
    #p[i] = pressure(R,V,L,dens,p,n)
#print  p 
cv_error = np.mean(cv_error)
print cv_error   
figcv = plt.figure()
plt.plot(np.transpose(t),np.transpose(cv))
plt.ylabel('C_v')
plt.title('Specific heat')
plt.show()

figet = plt.figure()
plt.title('Total energy')
plt.plot(np.transpose(t),ET)
plt.xlabel('time')
plt.ylabel('ET')
plt.show()

figcv.savefig('cv_1000.png')
figet.savefig('et_1000.png')
plt.plot(np.transpose(t),np.transpose(P))
plt.xlabel('time')
plt.ylabel('P')
plt.title('Pressure')
plt.show()

