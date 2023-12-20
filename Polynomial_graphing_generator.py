import numpy as np
import matplotlib.pyplot as plt

# Generate a random polynomial function
coefficients = np.random.uniform(-5, 5, size=np.random.randint(2, 6))  # Random coefficients
poly_function = np.poly1d(coefficients)  # Creating the polynomial function

# Define the interval [c, d]
c, d = -5, 5

# Generate points for plotting the polynomial function in the interval [c, d]
y_vals = np.linspace(c, d, 100)
x_vals = poly_function(y_vals)

# Plotting the polynomial function
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='g(y)', color='blue')


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid()
plt.show()



