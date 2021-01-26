"""
This module illustrates how to generate a three-dimensional plot and a 
contour plot.

For the example, the f(x,y) = x**2 * y**3 will be reproduced.
"""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

X = np.linspace(-2, 2)
Y = np.linspace(-1, 1)

x, y = np.meshgrid(X, Y)
z = x**2 * y**3

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(x, y, z)
ax.set_xlabel("$x$", usetex=True)
ax.set_ylabel("$y$", usetex=True)
ax.set_zlabel("$z$", usetex=True)
ax.set_title("Graph of the function $f(x,y) = x^2y^3$", usetex=True)

plt.show()

fig, ax = plt.subplots()
ax.contour(x, y, z)
ax.set_title("Contour of $f(x) = x^2y^3$", usetex=True)
ax.set_xlabel("$x$", usetex=True)
ax.set_ylabel("$y$", usetex=True)

plt.show()
