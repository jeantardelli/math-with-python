"""
Unfortunately, most functions are not linear and usually don't have nice
properties that we would like. For these non-linear functions, we cannot use the
fast algorithms that have been developed for linear problems, so we need to
devise new methods that can be used in these more general cases. One
general-purpose method, called the Nelder-Mead algorthim, is used to find the
minimum value of a function and does not rely on the gradient of the function.

This module illustrates how to use the Nelder-Mead simplex method to minimize
a non-linear function containing two variables.
"""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize

def func(x):
    return ((x[0] - 0.5)**2 + (x[1] + 0.5)**2)*np.cos(0.5*x[0]*x[1])

x_r = np.linspace(-1, 1)
y_r = np.linspace(-2, 2)
x, y = np.meshgrid(x_r, y_r)
z = func([x, y])

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(projection="3d")
ax.tick_params(axis="both", which="major", labelsize=9)
ax.set(xlabel="x", ylabel="y", zlabel="z")
ax.set_title("Objective function")
ax.plot_surface(x, y, z, alpha=0.7)

x0 = np.array([-0.5, 1.0])
ax.plot([x0[0]], [x0[1]], func(x0), "r*")

result = optimize.minimize(func, x0, tol=1e-6, method="Nelder-Mead")
print(result)

ax.plot([result.x[0]], [result.x[1]], [result.fun], "r*")
plt.show()

