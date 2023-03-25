import numpy as np
import matplotlib.pyplot as plt

# Define the original points
points = np.array([[1, 1], [2, 2], [3, 1]])

# Define the translation vector
t = np.array([2, 3])

# Define the transformation matrix
T = np.array([[1, 0, t[0]], [0, 1, t[1]], [0, 0, 1]])

# Apply the transformation
points_transformed = np.dot(T, np.hstack((points, np.ones((points.shape[0], 1)))).T).T[:, :-1]

# Plot the original and transformed points
plt.plot(points[:, 0], points[:, 1], 'ro', label='Original Points')
plt.plot(points_transformed[:, 0], points_transformed[:, 1], 'bo', label='Transformed Points')
plt.legend()
plt.show()
