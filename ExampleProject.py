from MyClasses import *
from MyMethods import fibonacciNum

# This examples main function
if __name__ == "__main__":
    print('This is a simple logistic regression training code')
    # The model will learn a simple prediction where f(x)=x/10

    # read the sample dataset
    ds = Dataset('ExampleCSV.csv')
    # init the model with the dataset
    model = Model(ds)
    # train the model
    model.train()
    # test the model
    model.test()
    print('Success!')

    # and now for the real magic - reacursive fibonacci for each label in the dataset
    labels=ds.df[1].values
    for label in labels:
        print(f'fibonacci({label}) = {fibonacciNum(label)}')
