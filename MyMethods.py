import numpy as np
import pandas as pd

# This file contains methods for my example project

# this function returns the Nth item in the fibonacci series
# but would eyal shanni describe it as poetry?
def fibonacciNum(N):
    if N <= 1:
        return N
    return fibonacciNum(N - 1) + fibonacciNum(N - 2)

# gets a csv file path and returns a pandas dataframe
def readCSV(filePath):
    data = pd.read_csv(filePath, header=None)
    return data

# this function gets a pandas series and returns the mean and std
def calcStats(series):
    mean = series.mean()
    std = series.std()
    return mean, std
