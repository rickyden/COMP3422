import matplotlib.pyplot as plt
import numpy as np


def series_part(t, k):
    # TODO: Define the inside-summation series part here
    x = 1 / np.pi / (2 * k + 1) * np.sin((2 * k + 1) * np.pi * t / 2) 
    return x


def series(t, K):
    # TODO: Define the series function here
    x = np.zeros_like(t)
    for k in range(K):
        x += series_part(t, k)
    return x


if __name__ == '__main__':
    # you are going to visualize the provided audio signal
    # TODO: initialize the time space
    t = np.linspace(-5,5,1000)

    # calculate the series result
    K = 50
    x = series(t, K)

    # TODO: plot the series
    plt.plot(t,x)
    pass

    plt.show()
