import numpy

def predict(features, weights):
    dot_product = numpy.dot(features, weights)
    return 1 if dot_product >= 0 else -1

def error_rate(x, y, weights):
    wrong_predictions = 0.0
    for i in range(len(x)):
        if predict(x[i], weights) != y[i]:
            wrong_predictions += 1
    return wrong_predictions / len(x)
