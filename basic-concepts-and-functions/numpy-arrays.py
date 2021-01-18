"""
This module contains basic manipulation with Numpy objects
"""
import numpy as np

arr = np.array([1, 2, 3, 4]) # array([1, 2, 3, 4])

first_element = arr[0] # 1
third_element = arr[2] # 3
even_idx = arr[::2] # array([1, 3])
first_two = arr[:2] # array([1, 2])

print(np.array([1, 2, 3, 4], dtype=np.float32))

print(arr.dtype) # dtype('int64')
arr.dtype = np.float32
print(arr)

arr = np.array([1, 2, 3, 4])
arr = arr.astype(np.float32)
print(arr)
