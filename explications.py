import numpy as np
import matplotlib.pyplot as plt


T = np.linspace(-1,1.5,1000)
h = 10**(-10)
f = lambda t : (-0.6*np.power(t, 3)+ 1.3*np.power(t, 3) + t - 0.8, t)
fprime = lambda t : (f(t+h)-f(t))/h

#La fonction
plt.plot(f(T)[0], f(T)[1], label = "Ligne de niveau à trouver")

#Les points
for x,y,name,col in [(-2,-0.8175, "$M_0$", "red"), 
                 (-0.5,-0.1875, "$M_1'$", "green"), (-0.643,0.154, "$M_1$", "red"), 
                 (0.5,1.297, "$M_2'$", "green"), (0.822,0.974, "$M_2$", "red")] :
    plt.scatter(x,y, s=100, c=col)
    plt.text(x + 0.03, y + 0.2 , name, fontsize=16)

#Les droites
X = np.linspace(-2,3,1000)
plt.plot(X, 0.42*(X+2) + -0.8175)
plt.plot(X, -1/0.42*(X+0.5) + -0.1875)
plt.plot(X, 1*(X+0.643) + 0.154)
plt.plot(X, -1*(X-0.5) + 1.297)

plt.xlim(-2, 3)
plt.ylim(-1, 2)
plt.legend()
plt.show()
