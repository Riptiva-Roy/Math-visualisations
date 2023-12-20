import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
R = 2  # Major radius of the torus
r = 0.5  # Minor radius of the torus

# Create a grid of theta and phi values for visualization
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 3 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for a part of the torus
x = (R + r * np.cos(phi)) * np.sin(theta)
y = r * np.sin(phi)
z = -(R + r * np.cos(phi)) * np.cos(theta)  # Negate z for inner visualization

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the torus section
ax.plot_surface(x, y, z, color='yellow')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Adjust viewing angle
ax.view_init(elev=20, azim=-45)

# Set aspect ratio for a natural look and show the plot
ax.set_box_aspect([1, 0.5, 1])
plt.show()

