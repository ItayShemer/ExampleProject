from MyMethods  import *
from sklearn.linear_model import LinearRegression
# This file contains classes for my example project

# this is an example dataset class
class Dataset:
    def __init__(self, filePath):
        self.df=readCSV(filePath)
        self.filePath=filePath

    # prints mean and std for a column of the dataset
    def printColumnStats(self,column):
        stats = calcStats(self.df[column])
        print(f'Mean = {stats[0]}')
        print(f'Std = {stats[1]}')

    # both getTrain and getTest aren't ideal but i wrote it quickly
    # returns training set that includes rows num of rows
    def getTrain(self , rows):
        return self.df.truncate(before=0, after=rows-1)

    # returns testing set that includes rows num of rows from the end of the dataset
    def getTest(self, rows):
        numSamples=len(self.df)
        return self.df.truncate(before=numSamples-rows, after=numSamples)

class Model:
    def __init__(self, dataset):
        self.dataset=dataset
        self.model=LinearRegression()

    # train the model
    def train(self):
        train = self.dataset.getTrain(5)
        x = train[0].values.reshape(-1, 1)
        y = train[1].values
        self.model.fit(x, y)

    # test the model (not scoring because i only have a single test sample)
    def test(self):
        test = self.dataset.getTest(1)
        x=test[0].values.reshape(-1, 1)
        print('testing model')
        print(f'Predict for x= {x}')
        print('prediction:')
        print(self.model.predict(x))

    # returns the model
    def getModel(self):
        return self.model
