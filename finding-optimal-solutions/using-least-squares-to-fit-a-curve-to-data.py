"""
Least squares is a powerful technique for finding a function from a relatively
small family of potential functions that best describe a particular set of data.
This technique is especially common in statistics. For example, least squares
is used in linear regression problems – here, the family of potential functions
is the collection of all linear functions. Usually, this family of functions
that we try to fit has relatively few parameters that can be adjusted to
solve the problem.

The idea of least squares is relatively simple. For each data point, we compute
the square of the residual – the difference between the value of the point and
the expected value given a function – and try to make the sum of these squared
residuals as small as possible (hence least squares).

This module illustrates how to use least squares to fit a curve to a sample set
of data.
"""
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a*x**2 + b*x + c

rng = default_rng(12345)
SIZE = 100
x_data = rng.uniform(-3.0, 3.0, size=SIZE)
noise = rng.normal(0.0, 0.8, size=SIZE)
y_data = 2.0*x_data**2 - 4*x_data + noise

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.set(xlabel="x", ylabel="y", title="Scatter plot of sample data")

coeffs, _ = curve_fit(func, x_data, y_data)
print(coeffs)
# [ 1.99611157 -3.97522213  0.04546998]

x = np.linspace(-3.0, 3.0, SIZE)
y = func(x, coeffs[0], coeffs[1], coeffs[2])
ax.plot(x, y, "k--")

plt.show()
