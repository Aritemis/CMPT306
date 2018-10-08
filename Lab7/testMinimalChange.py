'''
Unit test that tests implementation of permutate() function.
'''
import unittest

import MinimalChange

class Test(unittest.TestCase):

    def testMinimalChange(self):
        # list of size 1
        result = MinimalChange.permutate(1)
        trueresult = [(1,)]
        self.assertEqual(result, trueresult)

        # list of size 2
        result = MinimalChange.permutate(2)
        trueresult = [(1,2),(2,1)]
        self.assertEqual(result, trueresult)

        # list of size 3
        result = MinimalChange.permutate(3)
        trueresult = [(1, 2, 3), (1, 3, 2), (3, 1, 2), (3, 2, 1), (2, 3, 1), (2, 1, 3)]
        self.assertEqual(result, trueresult)

        # list of size 4
        result = MinimalChange.permutate(4)
        trueresult = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 4, 2, 3), (4, 1, 2, 3), (4, 1, 3, 2), (1, 4, 3, 2), (1, 3, 4, 2), (1, 3, 2, 4), (3, 1, 2, 4), (3, 1, 4, 2), (3, 4, 1, 2), (4, 3, 1, 2), (4, 3, 2, 1), (3, 4, 2, 1), (3, 2, 4, 1), (3, 2, 1, 4), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 3, 1), (4, 2, 3, 1), (4, 2, 1, 3), (2, 4, 1, 3), (2, 1, 4, 3), (2, 1, 3, 4)]
        self.assertEqual(result, trueresult)

if __name__ == "__main__":
    unittest.main()
