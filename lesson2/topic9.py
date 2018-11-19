import pandas as pd

# line equation
weight1 = 3
weight2 = 4
bias = -10

# point of analysis
point = (1, 1)

# learning rate
learning_rate = 0.1

# right answer
correct_output = 1

# actual answer
current_output = 0

# epochs
epochs = 0

while (current_output != correct_output):
    epochs = epochs+1
    print("Epoch {}".format(epochs))
    new_weight1 = weight1 + (point[0] * learning_rate * epochs)
    new_weight2 = weight2 + (point[1] * learning_rate * epochs)
    new_bias = bias + (1 * learning_rate * epochs)

    current_result = round((new_weight1 * point[0]) + (new_weight2 * point[1]) + new_bias, 2)

    current_output = 1 if current_result >= 0 else 0
