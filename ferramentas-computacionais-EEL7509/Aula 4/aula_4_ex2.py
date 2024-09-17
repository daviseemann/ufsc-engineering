import numpy as np


def matrix_gen(N):
    array = np.arange(1, (N * N) + 1, 1)
    matrix = array.reshape(N, N)
    return matrix.T


print(f"{matrix_gen(5) = } ")
