import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def main():
    weights = np.array([[2,6,-2],[3,5,-2.2],[5,4,-3]])
    probabilities = np.array([0.4, 0.6, 1])
    print(sigmoid(np.dot(weights, probabilities)))

if __name__ == "__main__":
    main()