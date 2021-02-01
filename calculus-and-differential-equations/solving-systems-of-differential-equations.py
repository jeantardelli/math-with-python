"""
This module illustrates how to solve a simple system of differential
equations. Consider the following, classic, Prey-Predator example:

    dP/dt = 5*P - 0.1*W*P
    dW/dt = 0.1*W*P - 6*W

where P is the prey specie and W, the predators. Note that this system
is a compete predator-prey example.
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate

def predator_prey_system(t, y):
    return np.array(
            [5*y[0] - 0.1*y[1]*y[0],
             0.1*y[1]*y[0] - 6*y[1]])

p = np.linspace(0, 100, 25)
w = np.linspace(0, 100, 25)
P, W = np.meshgrid(p, w)

dp, dw = predator_prey_system(0, np.array([P, W]))

fig, ax = plt.subplots()
ax.quiver(P, W, dp, dw)
ax.set_title("Population dynamics for two competing species")
ax.set_xlabel("P")
ax.set_ylabel("W")

initial_conditions = np.array([85, 40])

sol = integrate.solve_ivp(predator_prey_system, (0., 5.), 
                          initial_conditions, max_step=0.01)

ax.plot(initial_conditions[0], initial_conditions[1], "ko")
ax.plot(sol.y[0, :], sol.y[1, :], "k", linewidth=0.5)
plt.show()

fig, ax = plt.subplots()
ax.plot(sol.t, sol.y[0, :], 'k', label='P')
ax.plot(sol.t, sol.y[1, :], 'k-.', label='W')
ax.set_xlabel('t')
ax.set_ylabel('Population')
ax.set_title('Population against time')
ax.legend()
plt.show()
