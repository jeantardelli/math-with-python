"""
This module shows matrices as Numpy objects, emphasizing some matrix properties
and operations.
"""
import numpy as np
from numpy import linalg

np.eye(3)
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 1., 1.]])

mat = np.array([[1, 2], [3, 4]])
mat.transpose()
# array([[1, 3],
#        [2, 4]])
mat.T
# array([[1, 3],
#        [2, 4]])

A = np.array([[1, 2], [3, 4]])
A.trace() # 5

A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 1], [0, 1]])
A @ B 
# array([[-1, 3],
#        [0, 4]])
A * B
# array([[-1, 2],
#        [0, 4]])

A = np.array([[1, 2], [3, 4]])
I = np.eye(2)
A @ I
# array([[1, 2],
#        [3, 4]])

linalg.det(A) # -2.000000000000004
linalg.inv(A)
# array ([[-2. , 1. ]],
#         [1.5 , -0.5]])

Ainv = linalg.inv(A)
Ainv @ A
# Approximately
# array([[1., 0.]],
#        [0., 1.]])

A @ Ainv
# Approximetaly
# array([[1., 0.]],
#        [0., 1.]])
