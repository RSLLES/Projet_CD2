from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.power(x,2) + np.power(y,2)

def grad(f):
    """Retourne une fonction donnant le gradient de f"""
    h = 10**(-5)
    return lambda x,y : np.array((f(x+h,y)-f(x,y), f(x,y+h)-f(x,y)))/h

def creerPlan(f, x0, y0):
    """Retourne une fonction donnant le plan tangent en x0, y0 de f"""
    gradFEnM = grad(f)(x0,y0)
    return lambda x,y : gradFEnM[0]*(x-x0) + gradFEnM[1]*(y-y0) + f(x0,y0)

domain_x = np.linspace(-5, 5)   
domain_y = np.linspace(-5, 5)

X, Y = np.meshgrid(domain_x, domain_y)
Zf = f(X, Y)

x0,y0 = 2,2
z0 = f(x0,y0)
planEnM = creerPlan(f, x0, y0)
Zplan = planEnM(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Zf, cmap='winter')
ax.plot_surface(X, Y, Zplan, cmap='spring')

#ax.quiver3D(x0,y0,z0,gradf(x0,y0)[0], gradf(x0,y0)[1], 0, color="red")
plt.show()