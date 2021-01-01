# Use the apply function on existing columns with global variables as additional arguments.

import pandas as pd
import numpy as np


d = {'Min.Price': np.nanmean, 'Max.Price': np.nanmedian}

def apply_function(dataframe):
    df = dataframe[['Min.Price', 'Max.Price']]
    # apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.
    df.apply(lambda x, d: x.fillna(d[x.name](x)), args=(d,))
    print(df)
    return df


if __name__ == '__main__':
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    apply_function(df)
