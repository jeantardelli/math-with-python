"""
Bezier curves, or B-splines, are a family of curves that are extremely useful
in vector graphics – for instance, they are commonly used in high-quality font
packages. This is because they are defined by a small number of points that
can then be used to inexpensively calculate a large number of points along the
curve. This allows detail to be scaled according to the needs of the user.

This module illustrates how to create a simple class representing a Bezier
curve and compute a number of points along it.
"""
import numpy as np
import matplotlib.pyplot as plt

from math import comb as binom

class Bezier:

    def __init__(self, *points):
        self.points = points
        self.nodes = n = len(points) - 1
        self.degree = l = points[0].size
        self.coeffs = [binom(n, i)*p.reshape((l, 1))
                       for i, p in enumerate(points)]

    def __call__(self, t):
        n = self.nodes
        t = t.reshape((1, t.size))
        vals = [c @ (t**i)*(1-t)**(n-i) for i, c in enumerate(self.coeffs)]

        return np.sum(vals, axis=0)

p1 = np.array([0.0, 0.0])
p2 = np.array([0.0, 1.0])
p3 = np.array([1.0, 1.0])
p4 = np.array([1.0, 3.0])

fig, ax = plt.subplots()
ax.plot([0.0, 0.0, 1.0, 1.0], [0.0, 1.0, 1.0, 3.0], "*--k")
ax.set(xlabel="x", ylabel="y", title="Bezier curve with 4 nodes, degree 3")

b_curve = Bezier(p1, p2, p3, p4)
t = np.linspace(0, 1)
v = b_curve(t)

ax.plot(v[0, :], v[1, :])
plt.show()
