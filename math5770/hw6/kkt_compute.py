from sympy import symbols, Eq, solve

# Define the symbols
x1, x2, λ = symbols('x1 x2 λ')

# Define the equations based on the stationarity condition and the constraint
eq1 = Eq(2*x1 + 2*x2 - 3 - λ, 0)
eq2 = Eq(2*x1 + 4*x2 + 1 - λ, 0)
eq3 = Eq(1 - x1 - x2, 0)

# Solve the system of equations
solutions = solve((eq1, eq2, eq3), (x1, x2, λ))

print(solutions)

