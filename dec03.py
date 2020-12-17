# Write a funtion called generate_matrix_9x9() that generates a 9x9 matrix with all elements equal 2 except the one in the middle which should be equal 0. If you are not a beginner, set only the boundary entries to 2 and the remaining ones to 0 :)


import numpy as np


def generate_matrix_9x9():
    array = np.full((3, 3), 2)
    array[1, 1] = 0
    return array


if __name__ == '__main__':
    generate_matrix_9x9()
