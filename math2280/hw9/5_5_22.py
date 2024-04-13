import numpy as np
from scipy.linalg import eig
import sympy as sp

# Define the matrix A
A = np.array([[-15, -7, 4], [34, 16, -11], [17, 7, 5]])

# Compute the eigenvectors and eigenvalues
eigenvalues, eigenvectors = eig(A)

# Identify the repeated eigenvalue
repeated_eigenvalue = 2

# Construct the matrix of generalized eigenvectors
# Since there's only one eigenvector,
#  compute two generalized eigenvectors
P = np.column_stack((eigenvectors[:, 0],
        np.linalg.matrix_power(A -
        repeated_eigenvalue*np.eye(3), 1) @ eigenvectors[:, 0],
        np.linalg.matrix_power(A -
        repeated_eigenvalue*np.eye(3), 2) @ eigenvectors[:, 0]))

# Define the symbolic variables for time and constants
t, c1, c2, c3 = sp.symbols('t c1 c2 c3')

# Define the Jordan matrix
J = sp.Matrix(np.diag([repeated_eigenvalue]*3))
J[0, 1] = J[1, 2] = 1  # Filling the superdiagonal with 1's

# General solution
# x(t) = P * exp(J*t) * c, where c is the vector of constants
c = sp.Matrix([c1, c2, c3])
x_t = sp.Matrix(P) * sp.exp(J * t) * c

print(x_t)
