# Write a function called occurrences(data) that converts data (a dictionary) into series and returns the frequency count of of every number in this series.

import numpy as np
import pandas as pd


def occurrences(data):
    series = pd.Series(data)
    counts = series.value_counts()
    return counts


if __name__ == '__main__':
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    occurrences(days)
