#3D plot

def g(x, y):
    return x**2+y**2
z = g(2., 3.)
print z

#%matplotlib osx
#%matplotlib inline
from mpl_toolkits.mplot3d import axes3d #will make plot #3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm #color map

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
x = y = np.linspace(-5, 5, 100)
xv, yv = np.meshgrid(x, y)
z = g(xv, yv)
#ax.plot_wireframe(xv, yv, z, rstride = 1, cstride = 1, linewidth = 1) #if you cange rstride and cstride to 1, you'll have
                                                                        #finer plot, but takes longer to run

ax.plot_surface(xv, yv, z, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0)

plt.show()