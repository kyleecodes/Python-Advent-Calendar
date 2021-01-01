

# Write a function called get_joining_date(data) that takes as input a dictionary, turns it into Pandas dataframe, sets name as index, and returns the date on which Peter has joined the challenge :)

import numpy as np
import pandas as pd


def get_joining_date(dict):
    data = pd.DataFrame({'name': pd.Series(dict['name']), 'date_of_joining': pd.Series(dict['date_of_joining'])})
    data.set_index('name')
    return data.loc['name':'Peter', 'date_of_joining']


if __name__ == '__main__':
    dict = {'name': ['John', 'Mary', 'Peter', 'Jeff', 'Bill'],
            'date_of_joining': ['2020-11-25', '2020-11-26', '2020-11-30', '2020-11-27', '2020-12-01']}
    get_joining_date(dict)
