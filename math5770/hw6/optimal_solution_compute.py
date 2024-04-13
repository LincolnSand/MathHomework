import sympy as sp

# Define the variables
x1, x2, λ = sp.symbols('x1 x2 λ')

# Define the objective function
f = x1**2 + 2*x1*x2 + 2*x2**2 - 3*x1 + x2

# Compute the Hessian matrix
H = sp.hessian(f, (x1, x2))

# Check if the Hessian is positive semi-definite
H_eigenvalues = H.eigenvals()

# Define the Lagrangian
L = f + λ * (1 - x1 - x2)

# Compute the gradient of the Lagrangian
grad_L = [sp.diff(L, var) for var in [x1, x2, λ]]

# Solve the KKT conditions
kkt_points = sp.solve(grad_L, (x1, x2, λ), dict=True)

print(H)
print(H_eigenvalues)
print(kkt_points)

