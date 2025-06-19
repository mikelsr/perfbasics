from random import randint

_COLS = 3000
_ROWS = 3000

# Create a large square matrix using native Python lists
print("Creating matrix...", end="", flush=True)
MATRIX = [[randint(0, 100) for _ in range(_ROWS)] for _ in range(_COLS)]
print(" done.")


# Function to iterate over the matrix row by row
def iterate_by_row():
    total = 0
    size = len(MATRIX)
    for col in range(size):
        for row in range(size):
            total += MATRIX[col][row]
    return total


# Function to iterate over the matrix column by column
def iterate_by_column():
    total = 0
    size = len(MATRIX)
    for col in range(size):
        for row in range(size):
            total += MATRIX[row][col]
    return total
