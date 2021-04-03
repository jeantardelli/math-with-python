"""
Python is often criticized for being a slow programming language – a statement
that is endlessly debatable. Many of these criticisms can be addressed by
using a high-performance compiled library with a Python interface – such as
the scientific Python stack – to greatly improve performance. However, there
are some situations where it is difficult to avoid the fact that Python is not a
compiled language. One way to improve performance in these (fairly rare)
situations is to write a C extension (or even rewrite the code entirely in C) to
speed up the critical parts. This will certainly make the code run faster, but
it might make it more difficult to maintain the package. Instead, we can use
Cython, which is an extension of the Python language that is transpiled into C
and compiled for great performance improvements.

This module illustrates how to use Cython to greatly improve the performance of
code to generate an image of the Mandelbrot set.
"""
import time
import matplotlib.pyplot as plt

from functools import wraps

from mandelbrot.python_mandel import compute_mandel as compute_mandel_py
from mandelbrot.hybrid_mandel import compute_mandel as compute_mandel_hy
from mandelbrot.cython_mandel import compute_mandel as compute_mandel_cy

def timer(func, name):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        val = func(*args, **kwargs)
        t_end = time.time()
        print(f"Time taken for {name}: {t_end - t_start}")
        return val
    return wrapper

mandel_py = timer(compute_mandel_py, "Python")
mandel_hy = timer(compute_mandel_hy, "Hybrid")
mandel_cy = timer(compute_mandel_cy, "Cython")

Nx = 320
Ny = 240
steps = 255

mandel_py(Nx, Ny, steps)
mandel_hy(Nx, Ny, steps)
vals = mandel_cy(Nx, Ny, steps)

fig, ax = plt.subplots()
ax.imshow(vals.T, extent=(-2.5, 0.5, -1.2, 1.2))
plt.show()
