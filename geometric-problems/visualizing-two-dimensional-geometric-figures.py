"""
A geometric figure, at least in this context, is any point, line, curve, or
closed region (including the boundary) whose boundary is a collection of lines
and curves. Simple examples include points and lines (obviously), rectangles,
polygons, and circles.

This module shows how to visualize geometric figures using Matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

data = np.loadtxt("geometric-problems/swisscheese-grid-10411.csv")

fig, ax = plt.subplots()

outer = Circle((0.0, 0.0), 1.0, zorder=0, fc="k")
ax.add_patch(outer)

col = PatchCollection(
        (Circle((x, y), r) for x, y, r in data),
        facecolor="white", zorder=1, linewidth=0.2,
        ls="-", ec="k")
ax.add_collection(col)
ax.set_xlim((-1.1, 1.1))
ax.set_ylim((-1.1, 1.1))
ax.set_axis_off()

plt.show()
