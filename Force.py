# Force Function
import numpy as np
# Parameters
n = 10 # particle number
R = np.random.randint(0 , 100, (n,3)) # random init pos matric

#def force(R,n):
dx = np.zeros((n,n))
dy = np.zeros((n,n))
dz = np.zeros((n,n))
rho = np.zeros((n,n))
fx = np.zeros((n,n), dtype=float)
fy = np.zeros((n,n), dtype=float)
fz = np.zeros((n,n), dtype=float)
dU = np.zeros((n,n), dtype=float)

for i in range (n):
    for j in range (n):
        if i<j :
            
            dx[i,j] = R[i,0] - R[j,0]   #dx,dy,dz are elements of difference vector r_ij       
            dy[i,j] = R[i,1] - R[j,1]        
            dz[i,j] = R[i,2] - R[j,2]
        
            rho = ( dx**2 + dy**2 + dz**2)**0.5   # length of r_ij
            
            dU[i,j] = (12*rho[i,j]**-13 - 6*rho[i,j]**-7) * rho[i,j]**-1 # grad U
            
            fx[i,j] = dU[i,j] * dx[i,j] 
            fy[i,j] = dU[i,j] * dy[i,j]
            fz[i,j] = dU[i,j] * dz[i,j]
            
#force(R,n)