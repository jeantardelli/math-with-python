"""
This module shows matrix as Numpy objects, emphasizing some matrix properties.
"""
import numpy as np

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
