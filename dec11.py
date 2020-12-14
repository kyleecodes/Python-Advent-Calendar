# Write a function called multiply_with_transpose(m) that returns matrix m multiplied with its transpose. Think about what is special about M*M^T :)


import numpy as np


def multiply_with_transpose(m):
    transpose = np.transpose(m)
    matrix = np.matmul(m, transpose)
    return matrix


if __name__ == '__main__':
    m = np.array([[4, 1],
                  [2, 2]])
    multiply_with_transpose(m)
