'''
#HW03
#Terry Tran
#Partner: Jacob Baca

'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm #color map


def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):

    wave = (2./a)*((np.sin((n1*np.pi*x1)/a)*(np.sin((n2*np.pi*x2)/a)))-(np.sin((n1*np.pi*x2)/a)*(np.sin((n2*np.pi*x1)/a))))
    prob_dens = np.abs(wave)**2
    return wave, prob_dens

    
fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d')
plt.title('Wave Function')

ay = fig.add_subplot(122, projection = '3d')
plt.title('Probability Density')


plt.suptitle('Antisymmetric Spatial Wave Function')
x1 = x2 = np.linspace(-1, 1, 50)
xv, yv = np.meshgrid(x1, x2)


w, pd = antisym(xv, yv)

ax.plot_surface(xv, yv, w, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0)
ay.plot_surface(xv, yv, pd, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0)

fig.text(.1, 0, 'The "effective" interaction between two neutral Fermions (both spin up) that arises \n from the symmetry requirement on the total wave function.')
plt.show()