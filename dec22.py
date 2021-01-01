# Find all the local maxima (or peaks) in a numeric series.

import pandas as pd
import numpy as np


def get_maximas(series):
    dd = np.diff(np.sign(np.diff(series)))
    peak_locs = np.where(dd == -2)[0] + 1
    print(peak_locs)
    return peak_locs


if __name__ == '__main__':
    # Input
    ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
    get_maximas(ser)
