#Python Programming Assignment 4
#Addition of 2 Matrices using NumPy array

import numpy as np

matrix_A = np.array([[1, 2, 3], [4, 5, 6]])
matrix_B = np.array([[10, 20, 30], [40, 50, 60]])

result = matrix_A + matrix_B


print("Matrix A:")
print(matrix_A)
print("Matrix B:")
print(matrix_B)
print("Resulting Matrix after Addition:")
print(result)
