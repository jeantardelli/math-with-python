"""
This module illustrates how to use Matplolib subplots routine. This recipe
is useful when there is necessary to plot multiple related plots within the
same figure, side by side.
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_newton_iters(x0, number):
    """
    This function represents a Newton's method applied to the f(x)=x**2 - 1,
    with an initial value x0
    """
    iterates = [x0]
    errors = [abs(x0 - 1.)]
    for _ in range(number):
        x0 = x0 - (x0*x0 - 1.)/(2*x0)
        iterates.append(x0)
        errors.append(abs(x0 - 1.))
    return iterates, errors
        
# initial guess x0 = 2, 5 iterations
iterates, errors = generate_newton_iters(2.0, 5)

# 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

ax1.plot(iterates, "x")
ax1.set_title("Iterates")
ax1.set_xlabel("$i$", usetex=True)
ax1.set_ylabel("$x_i$", usetex=True)

# plot y on a logarithmic scale
ax2.semilogy(errors, "x")
ax2.set_title("Error")
ax2.set_xlabel("$i$", usetex=True)
ax2.set_ylabel("Error")

plt.show()
