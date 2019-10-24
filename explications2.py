import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def grad(f):
    """Retourne la fonction grad(f)"""
    h = 10**(-10)
    return lambda x,y : np.array((f(x+h,y)-f(x,y), f(x,y+h)-f(x,y)))/h


def creerPlanTg(f, x0, y0):
    """Retourne une fonction donnant le plan tangent en f(x0, y0)"""
    gradFEnM0 = grad(f)(x0,y0)
    return lambda x,y : gradFEnM0[0]*(x-x0) + gradFEnM0[1]*(y-y0) + f(x0,y0)


def f(x, y):
    """Fonction f avec laquelle on travaille"""
    return np.power(x,2) + np.power(y,2)
    #return np.exp(-10*(np.power(x-0.5,2)+np.power(y-0.5,2)))


## juste f
#Création du graphe en 3D
domain_x = np.linspace(0, 1)   
domain_y = np.linspace(0, 1)
X, Y = np.meshgrid(domain_x, domain_y)
fig = plt.figure()
ax = Axes3D(fig)

#On trace f
ax.plot_surface(X, Y, f(X, Y), cmap='winter')
ax.set_title("Fonction $f : x,y \longrightarrow x^2+y^2$")


##2) f avec plan tg
    
#On trace f
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x0,y0, f(x0,y0), s=500, c="red")
ax.plot_surface(X, Y, f(X, Y), cmap='winter')

#Test de tracé du plan tg en un point (x0,y0)
x0,y0 = 0.3,0.3
planEnM = creerPlanTg(f, x0, y0)
ax.plot_surface(X, Y, planEnM(X,Y), cmap='spring')
ax.set_title("Fonction $f$ et son plan tangant en $(0.3,0.3, f(0.3,0.3))$")
plt.show()


###3) Avec plan horizontal
#On trace f
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x0,y0, f(x0,y0), s=500, c="red")
ax.plot_surface(X, Y, f(X, Y), cmap='winter')

#Test de tracé du plan tg en un point (x0,y0)
x0,y0 = 0.3,0.3
planEnM = creerPlanTg(f, x0, y0)
ax.plot_surface(X, Y, planEnM(X,Y), cmap='spring')
# plan horizontal
ax.plot_surface(X, Y, f(0.3,0.3), cmap='spring')
ax.set_title("Fonction $f$, plan $z=c$ plan tangant à f en $(0.3,0.3, f(0.3,0.3))$")
plt.show()
