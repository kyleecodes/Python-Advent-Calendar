# Compute autocorrelations for the first 10 lags of ser. Find out which lag has the largest correlation.
# Lags are a feature of time series in Python. Best described as the classical way that time series forecasting problems are transformed into supervised learning problems. The simplest approach is to predict the value at the next time (t+1) given the value at the previous time (t-1)

import pandas as pd
import numpy as np


def autocorrelate_lag(series):
    autocorrelations = [series.autocorr(i).round(2) for i in range(11)]
    print(autocorrelations[1:])
    print('Lag having highest correlation: ', np.argmax(np.abs(autocorrelations[1:])) + 1)
    return


if __name__ == '__main__':
    ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
    autocorrelate_lag(ser)
