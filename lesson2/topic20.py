import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    CE = 0.0
    log_T = np.log(P)
    log_F = np.log(np.subtract(1, P))
    for i in range(len(Y)):
        CE = CE + (Y[i]*log_T[i]) + ((1-Y[i])*log_F[i])
    return -CE

def cross_entropy_solution(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))