__author__ = 'Jervis'
import random


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