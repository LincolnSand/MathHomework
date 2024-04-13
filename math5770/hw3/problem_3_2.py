import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1, 30)
y = 2*x**2 - 3*x + 1 + 0.05*np.random.randn(*x.shape)

A = np.zeros((x.size, 3))
for i in range(A.shape[1]):
    A[:,i] = x**i

coefficients = np.linalg.lstsq(A, y, rcond=None)[0]

print("{0:1.4f} x^2 + {1:1.4f} x + {2:1.4f}".format(coefficients[2], coefficients[1], coefficients[0]))

plt.plot(x, y, 'r.', x, A @ coefficients, 'b')
plt.xlim([0, 1])
plt.ylim([-0.4, 1])
plt.show()
