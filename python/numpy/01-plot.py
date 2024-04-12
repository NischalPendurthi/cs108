import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot with specified marker and line characteristics
plt.plot(x, y1, marker='o', color='blue', linestyle='--', label='sin(x)')
plt.plot(x, y2, marker='s', color='red', linestyle='-', label='cos(x)')

# Multiple plots with labels, title, grid
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)

# Subplots
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='green')
plt.title('Sin(x)')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='purple')
plt.title('Cos(x)')
plt.grid(True)

# Different plots: Scatter, Bar, Pie
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='orange', label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

plt.subplot(2, 2, 2)
x_bar = ['A', 'B', 'C', 'D', 'E']
y_bar = [3, 7, 2, 5, 8]
plt.bar(x_bar, y_bar, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.subplot(2, 2, 3)
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen', 'yellow'])

# Use of math functions
plt.figure()
plt.plot(x, np.exp(x), label='exponential')
plt.plot(x, np.log(x + 1), label='logarithm')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Math Functions')
plt.legend()

# Saving figures to a file
plt.savefig('plot.png')

# Show plots
plt.show()
