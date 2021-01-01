# Weight is the parameter within a neural network that transforms input data within the network's hidden layers. No worries - this task is not about implementing a neural network :)
# One of the important choices which have to be made before training a neural network consists in initializing the weight matrices since we don't know anything about the possible weights when we start. Write a function called initialize_weights(rows, columns) that returns a rows x columns matrix containing weights which are random uniform distributed over the half-open interval [0, 2).

# New code should use the uniform method of a default_rng() instance instead

import numpy as np


def initialize_weights(rows, columns):
    s = np.random.uniform(0, 2, size=(rows, columns))
    return s


if __name__ == '__main__':
    initialize_weights(5, 5)
