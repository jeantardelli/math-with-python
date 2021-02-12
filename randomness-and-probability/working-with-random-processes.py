"""
Random processes exist everywhere. Roughly speaking, a random process is a
system of related random variables, usually indexed with respect to time t ≥ 0,
for a continuous random process, or by natural numbers n = 1, 2, ..., for a
discrete random process.

This module examine the Poisson process, which is a simple yet interesing
random process.
"""
import matplotlib.pyplot as plt
import numpy as np

from numpy.random import default_rng
from scipy.special import factorial

def probability(events, param, time=1):
    return ((param*time)**events/factorial(events))*np.exp(-param*time)

rng = default_rng(12345)

rate = 4.0
inter_arrival_times = rng.exponential(scale=1./rate, size=50)

arrivals = np.add.accumulate(inter_arrival_times)
count = np.arange(50)

fig1, ax1 = plt.subplots()
ax1.step(arrivals, count, where="post")
ax1.set_xlabel("Time")
ax1.set_ylabel("Number of arrivals")
ax1.set_title("Arrivals over time")

N = np.arange(15)
estimated_scale = np.mean(inter_arrival_times)
estimated_rate = 1.0/estimated_scale

fig2, ax2 = plt.subplots()
ax2.plot(N, probability(N, param=rate), "k", label="True distribution")
ax2.plot(N, probability(N, param=estimated_rate), "k--",
         label="Estimated distribution")
ax2.set_xlabel("Number of arrivals in 1 time unit")
ax2.set_ylabel("Probability")
ax2.set_title("Probability Distribution")

plt.show()
