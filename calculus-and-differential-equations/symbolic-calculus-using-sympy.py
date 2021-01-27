"""
This module illustrates how to use SymPy to differentiate and integrate
a function that is not a simple polynomial
"""
import sympy

x = sympy.symbols('x')
f = (x**2 - 2*x)*sympy.exp(3 - x)

fp = sympy.simplify(sympy.diff(f))
fp2 = -(x**2 - 4*x + 2)*sympy.exp(3 - x)

sympy.simplify(fp2 - fp) == 0 # True

F = sympy.integrate(f, x) # -x**2*exp(3 - x)
