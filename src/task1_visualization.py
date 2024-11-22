import matplotlib.pyplot as plt
import numpy as np
import collections

def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    # Count the frequency of each category
    counter = collections.Counter(data)
    
    # Extract categories and their frequencies
    categories = list(counter.keys())
    frequencies = list(counter.values())
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(categories, frequencies, color=['red', 'blue', 'green'])
    
    # Add labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Categories')
    
    # Display the plot
    plt.show()
    return fig

# Example data: Random sampling from categories 'A', 'B', 'C'
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
