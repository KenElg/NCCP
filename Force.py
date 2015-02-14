# Force Function
import numpy as np

def force(R,n):
    dx = np.zeros((n,3))
    dy = np.zeros((n,3))
    dz = np.zeros((n,3))
#    rho1 = np.zeros((3,3))
    rho2 = np.zeros((n,3))
    fx = np.zeros((n,3), dtype=float)
    fy = np.zeros((n,3), dtype=float)
    fz = np.zeros((n,3), dtype=float)
    dU = np.zeros((n,3), dtype=float)

    for i in range (0,n):
        for j in range (0,n):       
            dx[i,j] = R[i,0] - R[j,0]   #dx,dy,dz are elements of difference vector r_ij       
            dy[i,j] = R[i,1] - R[j,1]        
            dz[i,j] = R[i,2] - R[j,2]
            rho2  = ( dx**2 + dy**2 + dz**2)**0.5   # length of r_ij
        
#           rho1 [i,j] =  ((R[i,0]-R[j,0])**2 + (R[i,1] - R[j,1])**2 + (R[i,2] - R[j,2])**2)**0.5
            dU[i,j] = 12*rho2[i,j]**-13 - 6*rho2[i,j]**-7 # grad U

            fx[i,j] = dU[i,j] * dx[i,j] * rho2[i,j]**-1
            fy[i,j] = dU[i,j]* dy[i,j] * rho2[i,j]**-1
            fz[i,j] = dU[i,j] * dz[i,j] * rho2[i,j]**-1

