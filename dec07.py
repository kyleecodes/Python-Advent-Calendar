

# Write a function called weighted_average(arr) that returns the weighted average of an input array where all elements besides the first and the last have the same weight and the weight of the 2 remaining ones is 5x bigger. For example, the weighted average for arr=np.array([1,2,3,4]) should be (5*1+1*2+1*3+5*4)/12 = 2.5. If you are a beginner - assume that the input array is 1-dimensional and it's length is >2. If you are NOT a beginner, try to make sure that this function also works for multi-dimensional arrays and doesn't break if the length of the input array is for example 1 (of course this is optional! :) )

import numpy as np


def weighted_average(arr):
    weighted = np.average(array)
    return weighted


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    weighted_average(array)