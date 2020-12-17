# We are half way there with the challenge and it's high time to play a bit with Pandas which is one of my favourites Python packages! :) Write a function called create_series(data) that takes as input a dictionary and converts it to a Pandas series.


import pandas as pd


def create_series(data):
    series = pd.Series(data)
    return series


if __name__ == '__name__':
    inp_dict = {'day_1': 100, 'day_2': 97, 'day_3': 94, 'day_4': 91, 'day_5': 88, 'day_6': 85, 'day_7': 82, 'day_8': 79,
                'day_9': 76, 'day_10': 73, 'day_11': 70}
    create_series(inp_dict)
