def f(x, y, R = 10, a = 1., b = 1.,): #decide rstride and cstride and color/				#colormap, plot a both inline and standalone
    return a*(x**2) - b*(y**2) - R**2


#%matplotlib inline
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
x = y = np.linspace(-5, 5, 100)
xv, yv, = np.meshgrid(x, y)
z = f(xv, yv)

ax.plot_surface(xv, yv, z, rstride = 5, cstride = 1, cmap = cm.coolwarm, linewidth = 0)
plt.show()