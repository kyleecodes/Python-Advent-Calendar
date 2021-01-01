# "ser" has missing dates and values, make all missing dates appear and fill up with value from previous dates

import numpy as np
import pandas as pd


def replace_missing_dates(series):
    print(series.resample('D').ffill())
    return series.resample('D').ffill()


if __name__ == '__main__':
    ser = pd.Series([1,10,3, np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
    replace_missing_dates(ser)
