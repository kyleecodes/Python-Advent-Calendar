# Dec 1st Challenge!
import numpy as np


# Write a function called generate_arr(start, end) that takes as input two integers start, end and returns a NumPy array (1 dimensional) containing all integers between those values including start and end.


def generate_arr(start, end):
    values = []
    list(map(lambda x: values.append(x), (i for i in range(start, end + 1))))
    array = np.array(values)
    print(array)
    return array


if __name__ == "__main__":
    generate_arr(2, 6)
