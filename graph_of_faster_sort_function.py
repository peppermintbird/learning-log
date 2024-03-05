import matplotlib.pyplot as plt
import numpy as np


# Define the functions
n = np.linspace(0, 20, 100)
function1 = 100 * n**2
function2 = 2**n

# Plot the functions
plt.figure(figsize=(8, 6))
plt.plot(n, function1, label='100n^2')
plt.plot(n, function2, label='2^n')

# Mark the intersection point
intersection_point = np.argwhere(np.diff(np.sign(function1 - function2)))[0]
plt.scatter(n[intersection_point], function1[intersection_point], color='red', label='Intersection Point')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Comparison of 100n^2 and 2^n')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
