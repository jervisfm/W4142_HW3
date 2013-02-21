from math import sqrt
from string import split
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib.mlab import stineman_interp


__author__ = 'Jervis'

def func(n):
    return 1 / np.sqrt(n)

def func2(x):
    return 1 / np.square(x)

def plot_file(file):
    f = open(file)

    line = f.readline()
    x = []
    y = []
    while line:
        row = split(line, ',')
        sample_size = long(row[0])
        y.append(sample_size)

        err = float(row[1])
        x.append(err)
        line = f.readline()


    fig = figure()
    plt.xlabel('Error')
    plt.ylabel('No Samples')
    print x
    print y


    plt.plot(x, y, 'r--', x,y, 'bo')

    plt.show()
    fig.savefig('graph.png')


def test():
    plot_file('data.csv')


test()