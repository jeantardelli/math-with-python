"""
This module illustrate how to find the roots of an equation using
the Newton-Rapshon and secant methods available in the Scipy lib.
"""
from scipy import optimize
from math import exp

def f(x):
    """Represents a mathematical function called f"""
    return x*(x - 2)*exp(3 - x)

def fp(x):
    """Represents the first derivative of f"""
    return -(x**2 - 4*x + 2)*exp(3 - x)

roots_secant = optimize.newton(f, 1., x1=1.5) # Using x1 = 1.5 and the secant
roots_newton = optimize.newton(f, 1., fprime=fp) # Using Newton-Rapshon method
roots_bisect = optimize.bisect(f, 1., 3) # Using bisect
roots_brent  = optimize.brentq(f, 1., 3.) # Using Brent 

print(roots_secant)
print(roots_newton)
print(roots_bisect)
print(roots_brent)
