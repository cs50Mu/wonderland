import scipy.io
from math import log

def make_binary(x):
    """ Convert all features in x to be binary (either 0 or 1).
    """
    for point in x:
        for i in range(len(point)):
            point[i] = 1 if point[i] > 0 else 0

def make_logarithmic(x):
    """ Convert all features in x to be logarithmic.
    """
    for point in x:
        for i in range(len(point)):
            point[i] = log(point[i] + 0.1)

def zero_to_minus_one(array):
    return [ (1 if y else -1) for y in array ]

def read_data(file='spamData.mat'):
    data = scipy.io.loadmat('spamData.mat')

    xtrain, xtest = data['Xtrain'], data['Xtest']
    # make_binary(xtrain)
    # make_binary(xtest)
    make_logarithmic(xtrain)
    make_logarithmic(xtest)

    ytrain, ytest = data['ytrain'], data['ytest']
    ytrain = zero_to_minus_one(ytrain)
    ytest = zero_to_minus_one(ytest)

    return xtrain, ytrain, xtest, ytest
