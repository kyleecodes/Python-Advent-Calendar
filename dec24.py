# Create a new column that contains the row number of nearest column by euclidean distance.

import pandas as pd
import numpy as np


def row_nearest_column(dataframe):
    nearest_rows = []
    nearest_distance = []
    for i, row in df.iterrows():
        curr = row
        rest = df.drop(i)
        e_dists = {}  # init dict to store euclidean dists for current row.
        # iterate rest of rows for current row
        for j, contestant in rest.iterrows():
            # compute euclidean dist and update e_dists
            e_dists.update({j: round(np.linalg.norm(curr.values - contestant.values))})
        # update nearest row to current row and the distance value
        nearest_rows.append(max(e_dists, key=e_dists.get))
        nearest_distance.append(max(e_dists.values()))

    df['nearest_row'] = nearest_rows
    df['dist'] = nearest_distance
    return


if __name__ == '__main__':
    df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
    row_nearest_column(df)


