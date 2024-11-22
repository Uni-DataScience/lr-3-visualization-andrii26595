import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Set Seaborn style for simplicity and readability
    sns.set(style="whitegrid")
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x='x', y='y', data=data, ax=ax, color='blue')
    
    # Add labels and title
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot of X vs Y')
    
    # Show the plot
    plt.show()
    
    return fig


# Example data: Generate 50 random values for x and y
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

# Call the function to create the scatter plot
create_scatter_plot(data)
