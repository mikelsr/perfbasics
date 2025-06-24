import argparse
import numpy as np
import requests


WEB_FILE_PREFIX = "https://github.com/mikelsr/perfbasics/raw/refs/heads/main/data/"


def serialize_matrix(matrix):
    """Converts a list of int lists (matrix) to a string format."""
    return "\n".join(" ".join(str(num) for num in row) for row in matrix)


def deserialize_matrix(text):
    """Converts a serialized matrix string back to a list of int lists."""
    if not text.strip():
        return []  # Handle empty input
    return [[int(num) for num in line.strip().split()] for line in text.strip().splitlines()]


def matrix_sum(matrix):
    np_matrix = np.array(matrix)
    return np_matrix.sum()


def from_file(matrix_file: str):
    with open(matrix_file, "r") as file:
        matrix_txt = file.read()
        return deserialize_matrix(matrix_txt)


def from_web(matrix_file: str):
    url = WEB_FILE_PREFIX + matrix_file
    res = requests.get(url)
    if res.status_code == 200:
        matrix_txt = res.text
        return deserialize_matrix(matrix_txt)
    else:
        raise Exception(f"Failed to fetch matrix from {url}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read and process a matrix from file or web.")
    parser.add_argument(
        "--source", choices=["file", "web"], required=True, help="Source of the matrix: 'file' or 'web'"
    )
    parser.add_argument("--path", required=True, help="File path or URL of the matrix source")

    args = parser.parse_args()

    if args.source == "file":
        matrix = from_file(args.path)
    elif args.source == "web":
        matrix = from_web(args.path)
    else:
        parser.print_help()
        exit(1)

    print("Sum of matrix elements:", matrix_sum(matrix))
