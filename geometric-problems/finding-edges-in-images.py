"""
Finding edges in images is a good way of reducing a complex image that contains
a lot of noise and distractions to a very simple image containing the most
prominent outlines. This can be useful as our first step of the analysis process,
such as in image classification, or as the process of importing line outlines
into computer graphics software packages.

This module shows how to use the scikit-image package and the Canny algorithm
to find the edges in a complex image.
"""
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.feature import canny

image = imread("geometric-problems/mandelbrot.png", as_gray=True)
edges = canny(image, sigma=0.5)

fig, ax = plt.subplots()
ax.imshow(edges, cmap="gray_r")
ax.set_axis_off()

plt.show()
