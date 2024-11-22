import numpy as np
import pandas as pd
import plotly.express as px


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Create the scatter plot
    fig = px.scatter(df, x='x', y='y', 
                     title="Interactive Scatter Plot", 
                     labels={'x': 'X Axis', 'y': 'Y Axis'})
    
    # Show the plot
    fig.show()


# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})

# Create the interactive scatter plot
create_interactive_plotly(df)
