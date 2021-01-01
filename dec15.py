# Write a function called where_is_2(series) that returns the position (integer) of the number 2.

import pandas as pd


def where_is_2(series):
    where_is_two = series.get_loc(2)
    return where_is_two


if __name__ == '__main__':
    my_list = [1, 6, 4, 9, 3, 0, 2]
    data = pd.Index(my_list)
    where_is_2(data)
