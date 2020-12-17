# Write a function called occurrences(series) that returns the frequency counts of number 2 of a given input series :)


import numpy as np
import pandas as pd


def occurrences(data):
    print(data.value_counts())
    return data.value_counts()


if __name__ == '__main__':
    s = pd.Series([1, 2, 3, 4, 2])
    occurrences(s)
