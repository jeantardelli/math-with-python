"""
Roughly speaking, a distribution function is a function f(x) that describes the
probability that a random variable has a value that is below x. In practical
terms, the distribution describes the spread of the random data over a range.
This module illustrates how to generate data following the normal distribution.
"""
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng

def normal_dist_curve(x):
    return 10000*np.exp(-0.5*((x-mu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))

rng = default_rng(12345)

mu = 5.0 # mean value
sigma = 3.0 # standard deviation
rands = rng.normal(loc=mu, scale=sigma, size=10000)

x_range = np.linspace(-5, 15)
y = normal_dist_curve(x_range)

fig, ax = plt.subplots()

ax.hist(rands, bins=20)
ax.plot(x_range, y, "k--")
ax.set_title("Histogram of normally distributed data")
ax.set_xlabel("Value")
ax.set_ylabel("Density")

plt.show()
