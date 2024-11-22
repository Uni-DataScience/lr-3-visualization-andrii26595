import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def perform_eda(df):
    """
    Performs Exploratory Data Analysis (EDA) including descriptive statistics, outlier detection,
    and correlation analysis.
    
    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # 1. Descriptive Statistics
    print("Descriptive Statistics:")
    print(df.describe())
    print("\n")

    # 2. Outlier Detection using Boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df)
    plt.title('Boxplot for Outlier Detection')
    plt.show()
    
    # 3. Correlation Analysis
    correlation_matrix = df.corr()
    print("Correlation Matrix:")
    print(correlation_matrix)
    print("\n")
    
    # Visualize Correlation Matrix using Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})

# Perform EDA on the dataset
perform_eda(df)
