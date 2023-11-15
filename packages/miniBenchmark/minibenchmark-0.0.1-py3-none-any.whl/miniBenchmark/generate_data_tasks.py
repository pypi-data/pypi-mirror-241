"""
This module provides functions to generate various types of datasets, random invertible matrices,
and specific waveforms for simulations and analysis.

Functions:
- generate_invertible_matrix(n, seed=42): 
    Generates a random invertible matrix of size n x n with a given random seed for reproducibility.
    
- generate_dataset(M, n, task='classification', n_classes=2, random_state=42, **kwargs): 
    Generates a dataset for machine learning tasks, creating data suitable for classification or 
    regression tasks using scikit-learn's `make_classification` or `make_regression`.
    
- generate_wave(r, n, intervals): 
    Generates a waveform based on the summation of a series of sine functions, each with 
    increasing frequency and amplitude defined by a base multiplier 'r'.

The functions in this module assist in creating synthetic data and waveforms for testing, 
machine learning model training, benchmarking, and other analytical purposes. Fixed random seeds 
ensure reproducibility of the generated datasets and matrices.

Example usage:
To generate a random invertible matrix:
    `matrix = generate_invertible_matrix(n=4, seed=42)`

To generate a dataset for a classification task:
    `ids, X, y = generate_dataset(M=100, n=4, task='classification', n_classes=3, random_state=42)`

To generate a dataset for a regression task:
    `ids, X, y = generate_dataset(M=100, n=4, task='regression', random_state=42)`

To generate a waveform with specific parameters:
    `wave = generate_wave(r=1, n=5, intervals=1000)`

Dependencies:
- numpy: Required for numerical operations, matrix generation, and waveform calculations.
- sklearn: Required for generating synthetic datasets for machine learning tasks.
"""

import numpy as np
from sklearn.datasets import make_classification

from sklearn.datasets import make_classification, make_regression
import numpy as np

def generate_dataset(M, n, task='classification', n_classes=2, random_state=42, **kwargs):
    """
    Generates an M*n dataset using sklearn's make_classification or make_regression.
    
    Parameters:
    - M (int): Number of samples
    - n (int): Number of features
    - task (str): Type of task to generate data for ('classification' or 'regression')
    - n_classes (int): Number of classes for classification task
    - random_state (int): Seed for the random number generator
    - **kwargs: Other arguments for make_classification or make_regression
    
    Returns:
    - ids (np.ndarray): ID array for samples
    - X (np.ndarray): Input data matrix
    - y (np.ndarray): Target values/labels
    """
    
    # Generate IDs
    ids = np.arange(1, M+1)
    
    if task == 'classification':
        X, y = make_classification(n_samples=M, n_features=n, n_classes=n_classes, random_state=random_state, **kwargs)
    elif task == 'regression':
        # Use make_regression for generating regression data
        X, y = make_regression(n_samples=M, n_features=n, random_state=random_state, **kwargs)
    else:
        raise ValueError("The 'task' parameter should be either 'classification' or 'regression'")
    
    return ids, X, y

# Example usage
# M = 100  # number of samples
# n = 4    # number of features
# ids, X, y = generate_dataset(M, n, task='regression', random_state=42)


# Example usage:
##ids, X, y = generate_dataset(100, 5, task='classification', n_classes=2)
#print(ids[:5])  # First 5 IDs
#print(X[:5])  # First 5 rows of data
#print(y[:5])  # First 5 labels/targets





import numpy as np

def generate_wave(r, n, intervals):
    """
    Generates a wave based on the summation of r*sin(pi*x) + r^2*sin(2*pi*x) + ... + r^n*sin(n*pi*x).
    
    Parameters:
        r (float): The base multiplier for the sine components.
        n (int): The number of terms in the wave equation.
        intervals (int): The number of constant intervals between 0 and 2*pi.
    
    Returns:
        np.ndarray: The resulting wave as an array of values.
    """
    
    # Create an array of x values from 0 to 2*pi with the specified number of intervals
    x = np.linspace(0, 2 * np.pi, intervals)
    
    # Initialize the wave as a zero array of the same length as x
    wave = np.zeros_like(x)
    
    # Add each term of the series to the wave
    for i in range(1, n + 1):
        wave += (r ** i) * np.sin(i * np.pi * x)
    
    return wave

# Example usage:
# Generate a wave with r = 1, n = 5 terms, and 1000 intervals
#r = 1
#n = 5
#intervals = 1000
#wave = generate_wave(r, n, intervals)

# If you want to plot the wave, you can use matplotlib
# import matplotlib.pyplot as plt
# plt.plot(wave)
# plt.show()


import numpy as np

def generate_invertible_matrix(n, seed=42):
    """
    Generates a random invertible matrix of size n x n.

    Parameters:
        n (int): The size of the matrix.
        seed (int, optional): The seed for the random number generator. Defaults to 42.

    Returns:
        np.ndarray: An invertible matrix.

    Raises:
        ValueError: If an invertible matrix cannot be generated.
    """
    np.random.seed(seed)  # Set the random seed for reproducibility
    
    max_attempts = 100
    for _ in range(max_attempts):
        # Generate a random matrix
        matrix = np.random.rand(n, n)
        # Check if the matrix is invertible by looking at its determinant
        if np.linalg.det(matrix) != 0:
            return matrix
    # If we reach here, we failed to generate an invertible matrix after max_attempts
    raise ValueError(f"Failed to generate an invertible matrix after {max_attempts} attempts.")

# Example usage:
#n = 4  # Size of the matrix
#matrix = generate_invertible_matrix(n)
#print("Random Invertible Matrix:")
#print(matrix)

    
