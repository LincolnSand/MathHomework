import cvxpy as cp
import numpy as np

# Generate the random points like the given Matlab code
np.random.seed(314)
x = np.random.rand(40, 1)
y = np.random.rand(40, 1)
classes = (2 * x < y + 0.5) + 1
A1 = np.hstack([x[classes.flatten() == 1], y[classes.flatten() == 1]])
A2 = np.hstack([x[classes.flatten() == 2], y[classes.flatten() == 2]])

# Define the optimization variables
w = cp.Variable(2)
b = cp.Variable()

# Define the constraints
constraints = [w.T @ A1[i] + b >= 1 for i in range(A1.shape[0])]
constraints += [w.T @ A2[i] + b <= -1 for i in range(A2.shape[0])]

# Define the objective function
objective = cp.Minimize(0.5 * cp.norm(w, 2)**2)

# Define the problem and solve
problem = cp.Problem(objective, constraints)
problem.solve()

# Extract the solution
w_value = w.value
b_value = b.value

print("The optimal w is:", w_value)
print("The optimal b is:", b_value)
