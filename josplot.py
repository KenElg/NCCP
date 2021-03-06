# josplot.py --- Animation
import numpy as np
#plotting
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# 3D plotting
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import juggle_axes
class AnimatedScatter(object):
    """
    Class for particle animation
    constructor takes as arguments
    -- numpoints: the number of points
    -- box_len: the side of the (cubic) box
    -- pos: numpy array of shape [numpoints, 3] containing the position coordinates
    -- mom: numpy array of shape [numpoints, 3] containing the momentum coordinates
    -- part_update: function which calculates the new particle positions
    This function must output the updated arrays pos and mom
    -- args: the function part_update takes as arguments numpoints, box_len, pos, mom, *args
    Example: anim_md.AnimatedScatter(n, box_len, pos, simulate, mom, n_t, dt)
    where 'simulate' is defined as
    def simulate(n, box_len, pos, mom, arglist):
    ...
    ...
    return pos, mom
    """
    def __init__(self, n, L, R, V, update_func, dt, tf,T):    
        self.numpoints = n
        self.pos = R
        self.mom = V
        self.box_len = L
        self.arglist = dt, tf, T
        self.stream = self.data_stream()
        self.angle = 30
        self.part_update = update_func
        self.fig = plt.figure(figsize=(16,12))
        self.FLOOR = 0.0
        self.CEILING = self.box_len
        self.ax = self.fig.add_subplot(111,projection = '3d')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=1,init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """ Set world coordinates, colors, symbol siez ('s') """
        x, y, z = next(self.stream)
        c = ['b']
        self.scat = self.ax.scatter(x, y, z,c=c, s=10, animated=True)
        self.ax.set_xlim3d(self.FLOOR, self.CEILING)
        self.ax.set_ylim3d(self.FLOOR, self.CEILING)
        self.ax.set_zlim3d(self.FLOOR, self.CEILING)
        return self.scat,
    def data_stream(self):
        """
        Calls particle update routine, copies it to the relevant section of the 'data' array which
        is then yielded
        """
        self.pos, self.outlist = self.part_update(self.numpoints, self.box_len, self.pos, self.mom, *self.arglist)
        data = np.transpose(self.pos)
        while True:
            self.pos, self.mom = self.part_update(self.numpoints, self.box_len, self.pos, self.mom, *self.arglist)
            data[:3, :] = np.transpose(self.pos)
            yield data
    def update(self, i):
        """ Use new particle position for drawing next frame """
        data = next(self.stream)
        data = np.transpose(data)
        self.scat._offsets3d = juggle_axes(data[:,0],data[:,1],data[:,2], 'z')
        self.ax.view_init(30,self.angle)
        plt.draw()
        return self.scat,
    def show(self):
        plt.show()
