# # Write a function called compute_percentage_unique_elements(arr) that returns the percentage of all unique entries of an array (as float). For example, the percentage of all unique entries of the 2-dimensional array [[1,2], [3,1]] is 75.

import numpy as np


def compute_percentage_unique_elements(arr):
    unique = np.unique(arr)
    unique_size = np.size(unique)
    original_size = np.size(arr)
    percent = unique_size / original_size
    return percent


if __name__ == '__main__':
    array = np.array([[1, 2], [3, 1]])
    compute_percentage_unique_elements(array)