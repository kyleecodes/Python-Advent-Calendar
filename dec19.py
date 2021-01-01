# Import every 50th row of BostonHousing dataset as a dataframe.

import pandas as pd
import numpy as np

if __name__ == '__main__':
    # Use chunks and list comprehension
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
    df2 = pd.concat([chunk.iloc[0] for chunk in df], axis=1)
    df2 = df2.transpose()

    print(df2.head())