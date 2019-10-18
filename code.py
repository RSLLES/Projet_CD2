from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def find_seed(g, c=0, eps=2**(-26)):
    """Methode renvoyant un réel t de [0,1] tq g(t) = c.
    La fonction retourne une valueError si jamais (g(0)-c)(g(1)-c) > 0"""
    if (g(0)-c)(g(1)-c) > 0:
        raise ValueError("Erreur : aucune garantie qu'un t tel que g(t) = 0 existe !")
    #On fait de la dichotomie car il faut travailler avec le eps
    return dicho(lambda t : g(t) - c,0,1,eps)

def dicho(g,a,b,eps):
    """Méthode récursive utilisant le principe de la dichotomie pour exploiter le TVI"""
    m = a+b/2
    if b-a <= 2*eps:
        return m
    elif g(a)*g(m) <= 0:
        return dicho(g,a,m,eps)
    else:
        return dicho(g,m,b,eps)


def f(x, y):
    """Fonction f avec laquelle on travaille"""
    return np.power(x,2) + np.power(y,2)

def grad(f):
    """Retourne la fonction grad(f)"""
    h = 10**(-5)
    return lambda x,y : np.array((f(x+h,y)-f(x,y), f(x,y+h)-f(x,y)))/h

def creerPlan(f, x0, y0):
    """Retourne une fonction donnant le plan tangent en x0, y0 de f"""
    gradFEnM = grad(f)(x0,y0)
    return lambda x,y : gradFEnM[0]*(x-x0) + gradFEnM[1]*(y-y0) + f(x0,y0)


#Création du graphe en 3D
domain_x = np.linspace(-5, 5)   
domain_y = np.linspace(-5, 5)
X, Y = np.meshgrid(domain_x, domain_y)
fig = plt.figure()
ax = Axes3D(fig)

#On trace f
ax.plot_surface(X, Y, f(X, Y), cmap='winter')

#Test de tracé du plan tg en un point (x0,y0)
x0,y0 = 2,2
planEnM = creerPlan(f, x0, y0)
ax.plot_surface(X, Y, planEnM(X,Y), cmap='spring')

#Affichage
plt.show()