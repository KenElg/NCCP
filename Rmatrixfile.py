import numpy as np
def init_pos(pos):
    rows=6
    i=0
    n=4*rows**3
    R=np.zeros((n,3),dtype=float)
    for x in range(0,rows):
        for y in range(0,rows):
            for z in range (0,rows):
                R[i:i+4,:]=np.array([[0+x,0+y,0+z],[0.5+x,0.5+y,0+z],[0.5+x,0+y,0.5+z],[0+x,0.5+y,0.5+z]]) 
                i=i+4
    V=np.random.normal(0,1,(n,3))