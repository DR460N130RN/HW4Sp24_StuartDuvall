import numpy as np
from scipy.linalg import solve

# Define the coefficients and constants for the first matrix problem
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])

b1 = np.array([2, 12, 10])

# Solve the first matrix problem
x1 = solve(A1, b1)

# Define the coefficients and constants for the second matrix problem
A2 = np.array([[1, -10, 2, 4],
               [3, 1, 4, 12],
               [9, 2, 3, 4],
               [-1, 2, 7, 3]])

b2 = np.array([2, 12, 21, 37])

# Solve the second matrix problem
x2 = solve(A2, b2)

# Print the solutions nicely
print("Solution to the first matrix problem:")
print(x1)

print("\nSolution to the second matrix problem:")
print(x2)
