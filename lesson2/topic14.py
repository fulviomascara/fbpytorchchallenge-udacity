import numpy as np
import math

# Parameters
W = [[4],[5]]
b = -9

def stepFunction(X, W, b):
    return (np.matmul(X,W)+b)[0]

# Sigmoid Function
def sigmoidFunction(x):
    return (1/(1+math.exp(-x)))

# Test Answers
test_array = [[1, 1], [2, 4], [5, -5], [-4, 5]]

for i in range(len(test_array)):
    print("Sigmoid = {}".format(sigmoidFunction(stepFunction(test_array[i], W, b))))