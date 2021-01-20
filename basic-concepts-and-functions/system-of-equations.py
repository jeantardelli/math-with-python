"""
This module illustrates how to solve a system of equations using solve routine
and the linalg module.

Suppose we have the following system of equations:

    3x1 - 2x2 + x3 = 7
    x1 + x2 -2x3 = -4
    -3x1 -2x2 + x3 = 1

We can solve it by the single matrix equation:

    Ax = b
"""
import numpy as np
from numpy import linalg

A = np.array([[3, -2, 3],
              [1, 1, -2],
              [-3, -2, 1]])

b = np.array([7, -4, 1])

linalg.solve(A, b) # array([ 1., -1., 2.])
