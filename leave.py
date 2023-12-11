import numpy as np
import matplotlib.pyplot as plt

# Define the affine transformation matrices and translation vectors
A1 = np.array([[0, 0], [0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])
t1 = np.array([[0], [0]])
t2 = np.array([[0], [1.6]])
t3 = np.array([[0], [1.6]])
t4 = np.array([[0], [0.44]])

# Define the probabilities
p1, p2, p3, p4 = 0.01, 0.85, 0.07, 0.07

# Initialize the starting point
v = np.array([[0], [0]])  # Starting point

# Initialize arrays to store points for each iteration
points = [v.flatten()]

# Generate points for 10 iterations
for n in range(1, 11):
    k = np.random.rand()
    if k < p1:
        v = A1.dot(v) + t1
    elif k < p1 + p2:
        v = A2.dot(v) + t2
    elif k < p1 + p2 + p3:
        v = A3.dot(v) + t3
    else:
        v = A4.dot(v) + t4
    points.append(v.flatten())

# Function to plot points up to a given iteration
def plot_points(iteration):
    x_vals = [point[0] for point in points[:iteration + 1]]
    y_vals = [point[1] for point in points[:iteration + 1]]
    plt.figure(figsize=(6, 10))
    plt.scatter(x_vals, y_vals, color='green')
    plt.title(f'Barnsley Fern after {iteration} Iterations')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Plotting points for each of the first 10 iterations
for i in range(10):
    plot_points(i)

# Generating 10 images of visualization for the first 10 iterations on the coordinate plane

def apply_transformation(v, A, t):
    """Apply an affine transformation."""
    return A.dot(v) + t

# Initial point
v = np.array([[0], [0]])

# Pre-defined sequence of transformations for demonstration
transformations = [A2, A2, A2, A3, A2, A2, A4, A2, A3, A2]
translations = [t2, t2, t2, t3, t2, t2, t4, t2, t3, t2]

# Plot setup
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
axes = axes.flatten()

# Apply transformations and plot each iteration
for i in range(10):
    axes[i].plot(v[0], v[1], 'o', color='blue')
    axes[i].set_xlim(-3, 3)
    axes[i].set_ylim(0, 10)
    axes[i].grid(True)
    axes[i].set_title(f'Iteration {i+1}')
    
    # Apply the next transformation
    v = apply_transformation(v, transformations[i], translations[i])

plt.tight_layout()
plt.show()
