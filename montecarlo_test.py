__author__ = 'Jervis'

import unittest
from util import *
from montecarlo import *

class MyTestCase(unittest.TestCase):

    def test_cube_volume(self):
        x0 = -5
        x1 = 5
        y0 = -10
        y1 = -15
        z0 = 100
        z1 = 200
        val = cube_volume(x0,x1,y0,y1,z0,z1)
        ans = 10 * 5 * 100
        self.assertEqual(val, ans, "volumes computation failed:  %f vs %f " % (val,ans))
        self.assertEqual(True, True)

    def test_random_vector(self):
        size = 10
        start = 0
        end = 1
        list = random_vector(size, start, end)
        self.assertTrue(len(list) == size, "Vector not of right size")
        for x in xrange(0,size,1):
            val = list[x]
            self.assertTrue(val >= start and val <= end, "values in vector out of range")

if __name__ == '__main__':
    unittest.main()

