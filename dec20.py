# Filter words that contain at least 2 vowels from a series.

import pandas as pd
from collections import Counter


def two_vowels(series):
    mask = ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
    print(ser[mask])
    return ser[mask]


if __name__ == '__main__':
    ser = pd.Series(['Red', 'Orange', 'Pink', 'Python', 'Money'])
    two_vowels(ser)
