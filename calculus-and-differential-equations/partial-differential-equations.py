"""
This module illustrates how to solve a partial differential equation with
Python. The module takes as example the classic problem of a one dimensional
heat equation:

    partial u / partial t = a * [partial**2 u / (partial x) **2] + f(t,x)

where a is a positive constant and f(t,x) is a function. f(t,x) = 0, a = 1,
and L = 2. The boundary conditions are:

    u(t,0) = u(t,L) = 0 (t>0)

The temperature profile is:

    u(0,x) = 3 sin (pi*x/2) (0<=x<=2)

The finite differences is the method used to solve the partial differential eq.
"""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
from scipy import sparse

def initial_profile(x):
    return 3*np.sin(np.pi*x/2)

alpha = 1
x0 = 0 # left hand x limit
xL = 2 # Right hand x limit

N = 10
x = np.linspace(x0, xL, N+1)
h = (xL - x0)/N

k = 0.01
steps = 100
t = np.array([i*k for i in range(steps+1)])

r = alpha*k / h**2
assert r < 0.5, f"Must have r < 0.5, currently r={r}"

diag = [1, *(1-2*r for _ in range(N-1)), 1]
abv_diag = [0, *(r for _ in range(N-1))]
blw_diag = [*(r for _ in range(N-1)), 0]

A = sparse.diags([blw_diag, diag, abv_diag], (-1, 0, 1), shape=(N+1, N+1),
                 dtype=np.float64, format="csr")
u = np.zeros((steps+1, N+1), dtype=np.float64)

u[0,:] = initial_profile(x)

for i in range(steps):
    u[i+1, :] = A @ u[i, :]

X, T = np.meshgrid(x, t)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(T, X, u, cmap="hot")
ax.set_title("Solution of the heat equation")
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_zlabel("u")

plt.show()
