import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


def make_dis(n=10, mid=0, mu = 0.5, sig = 0.08):
    range_index = list(range(n))
    # x_values = [x+1 for x in range_index]
    x_values = [x - mid + n/2.for x in range_index]
    x_values = [(x + n) % n for x in x_values]
    x_values = np.array([x / n for x in x_values])
    mu, sig = 0.5, 0.05
    y_values = gaussian(x_values, mu, sig)
    y_values = y_values / sum(y_values)
    # plt.plot(range_index, y_values)
    # plt.show()
    return y_values


if __name__ == '__main__':
    make_dis(mid = 7.1)