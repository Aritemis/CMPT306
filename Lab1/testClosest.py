'''
@author: Ariana Fairbanks

'''

import unittest
import Closest

class Test(unittest.TestCase):
    def testClosest(self):
        expected = (-13,-14)
        self.assertEqual(expected,Closest.closest_pair([-13, 5, 18, 7, -14, 21]))

        expected = (-13,-13)
        self.assertEqual(expected,Closest.closest_pair([-13, 5, 18, 7, -14, -13]))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()













