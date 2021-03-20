"""
A geometric figure is said to be convex if every pair of points within the
figure can be joined using a straight line that is also contained within the
figure. Simple examples of convex bodies include points, straight lines,
squares, circles (disks), regular polygons, and so on.

Convex figures are simple from a certain perspective, which means they are
useful in a variety of applications. One particular problem involves finding
the smallest convex set that contains a collection of points. This smallest
convex set is called the convex hull of the set of points.

This module illustrates how to find the convex hull of a set of points using
the Shapely package.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy.random import default_rng
from shapely.geometry import MultiPoint

rng = default_rng(12345)
raw_points = rng.uniform(-1.0, 1.0, size=(50, 2))

fig, ax = plt.subplots()
ax.plot(raw_points[:, 0], raw_points[:, 1], "k.")
ax.set_axis_off()

points = MultiPoint(raw_points)
convex_hull = points.convex_hull
patch = mpl.patches.Polygon(convex_hull.exterior, alpha=0.5, ec="k", lw=1.2)
ax.add_patch(patch)

plt.show()
