from math import exp
from random import randint, randrange
import random
import subprocess
from time import localtime

__author__ = 'Jervis Muindi'

def hello():
    print('hello world from idea 9')

def f(x,y,z):
    # x^2*y + exp(-z)
    return x*x*y + exp(-z)

def monte_carlo():


    return None

def cube_volume(x0,x1,y0,y1,z0,z1):
    return abs(x0-x1) * abs(y0-y1) * abs(z0-z1)

def random_vector(size, start, end):
    if size == 0:
        return []

    if size < 0:
        size = abs(size)

    result = []
    for x in xrange(0,size,1):
        val = random.uniform(start,end)
        result.append(val)
    return result

def t():
    return [ 10, 20, 30]
def main():
    x = 2
    y = 3
    z = 3
    print "f(x,y,z) is %f" % (f(x,y,z))

    for x in xrange(0,10,1):
        r = random.uniform(0,20)
        print x

    l = [1, 2, 3, 4, 5]
    l.append(6)

    print l
    print t()

if  __name__ == '__main__':
    main()

#main()

