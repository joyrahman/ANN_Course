import math
import random


def sigmoid(x):
    return 1.0 / (1 + math.exp(-x))


def deriv_sigmoid(x):
    sgmd = sigmoid(x)
    return (1 - sgmd) * sgmd


def between(min, max):
    """
    Return a real random value between min and max.
    """
    return random.random() * (max - min) + min


def make_matrix(N, M):
    """
    Make an N rows by M columns matrix.
    """
    return [[0 for i in range(M)] for i in range(N)]
