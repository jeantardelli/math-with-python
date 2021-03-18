"""
One problem with working with two-dimensional figures in a programming
environment is that you can't possibly store all the points that lie within
the figure. Instead, we usually store far fewer points that represent the
figure in some way. In most cases, this will be a number of points (connected
by lines) that describe the boundary of the figure. This is efficient in terms
of memory and makes it easy to visualize them on screen using Matplotlib
Patches, for example. However, this approach makes it more difficult to
determine whether a point, or another figure, lies within a given figure. This
is a crucial question in many geometric problems.

This module illustrates how to represent geometric figures and determine whether
a point lies within a figure or not.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

from shapely.geometry import Polygon, Point

polygon = Polygon(
    [(0, 2), (-1, 1), (-.5, -1), (.5, -1), (1, 1)])

fig, ax = plt.subplots()
poly_patch = mpl.patches.Polygon(polygon.exterior, ec="k", lw="1", alpha=0.5)
ax.add_patch(poly_patch)
ax.set(xlim=(-1.05, 1.05), ylim=(-1.05, 2.05))
ax.set_axis_off()

p1 = Point(0.0, 0.0)
p2 = Point(-1.0, -.75)

ax.plot(0.0, 0.0, "k*")
ax.annotate("p1", (0.0, 0.0), (0.05, 0.0))
ax.plot(-.8, -.75, "k*")
ax.annotate("p2", (-.8, -.75), (-.8 + .05, -.75))

print("p1 inside polygon?", polygon.contains(p1))
print("p2 inside polygon?", polygon.contains(p2))

plt.show()
