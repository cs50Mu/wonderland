from read_data import read_data
from utils import error_rate, predict
import numpy

def update_weights(features, label, weights):
    """ Update and return the weights vector according to perceptron rules.
    It is assumed that the weights vector is supposed to be changed.
    """
    scaled_label = numpy.multiply(label, features)
    return numpy.add(weights, scaled_label)

def train_point(features, label, weights):
    """ Checks whether a single point is correctly classified.
    If it is not correctly classified, the weights vector is updated.
    Returns the new weights vector.
    """
    prediction = predict(features, weights)
    if prediction != label:
        weights = update_weights(features, label, weights)
    return weights

def train(x, y, num_iterations=5000):
    num_data_points = len(x)
    weights = numpy.zeros(len(x[0])) # Initialize weights to zeros
    for i in range(num_iterations):
        # if i % 100 == 0:
        #     print i
        for j in range(num_data_points):
            weights = train_point(x[j], y[j], weights)
    return weights

xtrain, ytrain, xtest, ytest = read_data()
weights = train(xtrain, ytrain)

# Probably want to print stuff here
# print weights
# print error_rate(xtrain, ytrain, weights)
# print error_rate(xtest, ytest, weights)
