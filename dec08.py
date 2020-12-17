# Data Scientists sometimes implement their own sophisticated metrics :) Write a funtion called calculate_magda_metric(arr) that takes as input a matrix and computes magda_metric which is the mean of the values in the first column multiplied by the sum of the values in the last row. For example, magda_metric for the following matrix: [[1,2], [3,5]] should be equal ((1+3)/2 * (3+5)) = 2*8 = 16 . If you know how - make sure this function doesn't break if the input matrix has only one row :)

import numpy as np


def calculate_magda_metric(arr):
    mean = np.mean(arr[:, 0])
    add = np.sum(arr[1])
    metric = mean * add
    return metric


if __name__ == '__main__':
    array = np.array([[1, 2], [3, 5]])
    calculate_magda_metric(array)
