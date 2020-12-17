# Write a funtion called get_elements(arr) that returns the median of all the elements of the input array which are greater than 2. If you are able to, make sure that this function works well even if one of the elements is numpy.nan :)


import numpy as np


def get_elements(arr):
    a = np.array(arr)
    greater_than_two = np.where(a > 2)
    new_array = np.median(greater_than_two)
    return new_array


if __name__ == '__main__':
    array = [1, 1, 1, 2, 4, 5, 6, 7, 8, 9]
    get_elements(array)
