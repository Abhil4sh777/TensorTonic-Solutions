import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    n = len(A)
    m = len(A[0]) if n > 0 else 0
    
    # Initialize B as an empty 2D list of shape (m, n)
    B = [[0] * n for _ in range(m)]
    
    # Fill B by swapping indices
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
            
    # Convert B to a NumPy array and return
    return np.array(B)
