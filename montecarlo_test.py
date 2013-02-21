__author__ = 'Jervis'

import unittest
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
        

if __name__ == '__main__':
    unittest.main()

