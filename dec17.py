# Write a function called get_joining_date(dict) that takes as input a dictionary (see example below, same as yesterday), turns it into Pandas dataframe, converts the column date_of_joining to datetime type, sets date_of_joining as index, and returns the name of the participant who joined the challenge on Dec 1st :)

import numpy as np
import pandas as pd


def get_joining_date(dict):
    # YOUR CODE GOES HERE
    return


if __name__ == '__main__':
    dict = {'name': ['John', 'Mary', 'Peter', 'Jeff', 'Bill'],
            'date_of_joining': ['2020-11-25', '2020-11-26', '2020-11-30', '2020-11-27', '2020-12-01']}
    get_joining_date(dict)
