# Dec 2nd Challenge!

# Missing data is an everyday problem that data scientists need to deal with. Write a function called replace_nans(array) that takes as input a NumPy array and returns it after replacing all np.nan (numpy.nan) values with -1.

# numpy.isnan(array [, out])

import numpy as np


def replace_nans(array):
    where_are_NaNs = np.isnan(array)
    array[where_are_NaNs] = -1
    return array


if __name__ == "__main__":
    array1 = np.array([2, 2, 2, np.NaN, 2, 2])
    replace_nans(array1)
