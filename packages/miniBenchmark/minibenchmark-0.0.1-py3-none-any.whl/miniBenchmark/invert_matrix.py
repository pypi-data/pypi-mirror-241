import numpy as np
from .generate_data_tasks import generate_invertible_matrix
def invert_matrix_cpu(matrix):
    """
    Inverts a matrix using CPU and NumPy.

    Parameters:
    - matrix (numpy.ndarray): The matrix to be inverted.

    Returns:
    - inverted_matrix (numpy.ndarray): The inverted matrix, or None if the matrix is singular.
    """
    try:
        inverted_matrix = np.linalg.inv(matrix)
        return inverted_matrix
    except np.linalg.LinAlgError:
        # The matrix is singular and cannot be inverted.
        return None

# Example usage:

#n = 2**13
#matrix = generate_invertible_matrix(n)
#inverted_matrix = invert_matrix_cpu(matrix)

def task_matrix_inversion(n):
    matrix = generate_invertible_matrix(n)
    inverted_matrix = invert_matrix_cpu(matrix)
    return None


