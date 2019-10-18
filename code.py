from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.power(x,2) + np.power(y,2)


domain_x = np.linspace(-5, 5)   
domain_y = np.linspace(-5, 5)

X, Y = np.meshgrid(domain_x, domain_y)
Z = f(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, cmap='winter')
#plt.show()