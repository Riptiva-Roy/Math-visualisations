import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Torus parameters
R = 2  # Major radius of the torus
r = 0.5  # Minor radius of the torus

# Create a grid of theta and phi values for the torus visualization
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for the torus surface
x_torus = (R + r * np.cos(phi)) * np.cos(theta)
y_torus = (R + r * np.cos(phi)) * np.sin(theta)
z_torus = r * np.sin(phi)

# Create a 3D figure for the torus
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the torus surface
ax.plot_surface(x_torus, y_torus, z_torus, cmap='viridis')

# Elliptic paraboloid parameters
u = np.linspace(0, 1.7, 100)
v = np.linspace(0, 2*np.pi, 100)
u, v = np.meshgrid(u, v)

# Parametric equations for the elliptic paraboloid surface
x_paraboloid = u * np.cos(v)
y_paraboloid = u * np.sin(v)
z_paraboloid = u**2

# Plot the elliptic paraboloid surface
ax.plot_surface(x_paraboloid, y_paraboloid, z_paraboloid, cmap='plasma')

# Set axis labels and show the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()




