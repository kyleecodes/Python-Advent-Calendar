# Write a function called create_and_sort_series(data) that takes as input a list of values, converts it to a Series, adds value 2 to the series, and returns a sorted version of it (descending!).


import numpy as np
import pandas as pd


def create_and_sort_series(data):
    series = pd.Series(data)
    add_2 = series.append(pd.Series([2]))
    return add_2.sort_values(ascending=False)


if __name__ == '__main__':
    inp = [1, 6, 4, 9, 3, 0]
    create_and_sort_series(inp)
