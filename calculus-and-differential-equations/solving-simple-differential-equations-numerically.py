"""
This modules shows the numerically solution of a differential equation with
Scipy. The problem framed is the Newton's law of cooling:

    dT/dt = -k*T

where k is a positive constant that determines the rate of cooling. The
solution has the general form:

    T(t) = T0 * exp(-k*t)
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate

# True solution
def true_solution(t):
    return 50*np.exp(-0.2*t)

# Define the general form of the differential equation (y -> T)
def f(t, y):
    return -0.2*y

# Time range
t_range = (0, 10)

# Initial temperature
T0 = np.array([50])

scipy_sol = integrate.solve_ivp(f, t_range, T0, max_step=0.1)

t_vals = scipy_sol.t
T_vals = scipy_sol.y[0, :]

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

ax1.plot(t_vals, T_vals)
ax1.set_xlabel("$t$", usetex=True)
ax1.set_ylabel("$T$", usetex=True)
ax1.set_title("Solution of the cooling equation")

err = np.abs(T_vals - true_solution(t_vals))
ax2.semilogy(t_vals, err)
ax2.set_xlabel("$t$", usetex=True)
ax2.set_ylabel("Error", usetex=True)
ax2.set_title("Error in approximation (RK4)")

plt.show()
