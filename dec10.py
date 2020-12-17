# Matrix multiplication is an important component of many scientific computing and machine learning tasks, and it is often the performance bottleneck for those tasks. Write a function called can_multiply(m1, m2) that takes as input a x b matrix m1 and c x d matrix m2 and returns true if it is possible to multiply m1 and m2 and false otherwise. For example, can_multiply(m1 = np.array([[1,2], [3,4]]), m2 = np.array([[1,2, 3], [4, 5, 6]])) should return true since it is possible to multiply m1 with the transpose of m2 (2x2 matrix multiplied by a 2x3 matrix s possible). If you are a beginner, assume that the input matrices cannot are 2-dimensional. If you are not a beginner, make sure your function doesn't break if one of the inputs is a 1-dim matrix.
# Remember, you can multiply two matrices if and only if the number of columns in the first matrix equals the number of rows in the second matrix.


import numpy as np


def can_multiply(m1, m2):
    first_columns = m1.shape[1]
    second_rows = m2.shape[0]
    if first_columns == second_rows:
        return True
    else:
        return False


if __name__ == '__main__':
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[1, 2, 3], [4, 5, 6]])
    can_multiply(m1, m2)
