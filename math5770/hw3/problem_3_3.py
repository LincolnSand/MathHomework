from circle_fit import taubinSVD
import matplotlib.pyplot as plt

def circle_fit(points):
    xc, yc, r, sigma = taubinSVD(points)
    return ((xc, yc), r)

points = [[0, 0], [0.5, 0], [1, 0], [1, 1], [0, 1]]

(x, r) = circle_fit(points)


circle = plt.Circle(x, r, color='r', fill=False)

for point in points:
    plt.scatter(point[0], point[1])

plt.gca().add_patch(circle)

plt.show()
