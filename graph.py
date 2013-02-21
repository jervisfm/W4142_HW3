from math import sqrt
from string import split
import matplotlib.pyplot as plt
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


    plt.xlabel('Error')
    plt.ylabel('No Samples')
    print x
    print y
    t1 = np.arange(10 ** (-5), 100, 10 ** (-4))

    yp = None

    xi = np.linspace(x[0],x[-1],1000)

    plt.plot(x, y, 'r--', x,y, 'bo')

    #plt.axis([0, 2*10 **6, 0, 100])
    #t1 = np.arange(1, 2*10**6, 100)

    #plt.axis([0, 40, -10, 10**6])


    #plt.plot( t1,func2(t1), 'b')

    
    plt.show()



def test():
    plot_file('data.csv')


test()