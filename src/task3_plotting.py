import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_1d(data):
    """
    Creates a 1D line plot for a sequence of values.

    Parameters:
    data (array-like): A sequence of data points to plot.
    """
    plt.figure(figsize=(6, 4))
    plt.plot(data, label='1D Line Plot', color='b')
    plt.title('1D Line Plot of Data')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_2d(x, y):
    """
    Creates a 2D scatter plot to show the relationship between two variables.

    Parameters:
    x (array-like): Data for the x-axis.
    y (array-like): Data for the y-axis.
    """
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='g')
    plt.title('2D Scatter Plot: X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def plot_3d(x, y, z):
    """
    Creates a 3D scatter plot using Axes3D.

    Parameters:
    x (array-like): Data for the x-axis.
    y (array-like): Data for the y-axis.
    z (array-like): Data for the z-axis.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='r')
    ax.set_title('3D Scatter Plot: X, Y, Z')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# Example data
x = np.linspace(0, 10, 100)  # For 1D and 2D data
y = np.sin(x)  # For 2D data
z = np.cos(x)  # For 3D data

# Create and display the plots
plot_1d(x)  # 1D Line Plot
plot_2d(x, y)  # 2D Scatter Plot
plot_3d(x, y, z)  # 3D Scatter Plot
