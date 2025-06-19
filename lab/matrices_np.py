import numpy as np

_COLS = 3000
_ROWS = 3000

# Create a large matrix using NumPy
print("Creating matrix...", end="", flush=True)
MATRIX = np.random.randint(0, 101, size=(_COLS, _ROWS))
print(" done.")


# Function to iterate over the matrix row by row
def iterate_by_row():
    total = 0
    for col in range(MATRIX.shape[0]):
        for row in range(MATRIX.shape[1]):
            total += MATRIX[col, row]
    return total


# Function to iterate over the matrix column by column
def iterate_by_column():
    total = 0
    for row in range(MATRIX.shape[1]):
        for col in range(MATRIX.shape[0]):
            total += MATRIX[col, row]
    return total


def matrix_sum():
    return np.sum(MATRIX)
