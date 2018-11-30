import unittest

from change_making import change_making
from climb_stair import climb_stair
from roll_dice import roll_dice

class Test(unittest.TestCase):

    def test_change_making(self):
        d = [1,2,3,4,5,6]
        n = 10
        self.assertEqual(2, change_making(d, n))

        d=[1,2,4,6,8,10,22,23]
        n=40
        self.assertEqual(3, change_making(d, n))

        d=[1,2,10,11,12,15,19,30]
        n=1900
        self.assertEqual(64, change_making(d, n))


    def test_climb_stair(self):
        n = 10
        self.assertEqual(89, climb_stair(n))

        n = 20
        self.assertEqual(10946, climb_stair(n))

        n = 30
        self.assertEqual(1346269, climb_stair(n))

    def test_roll_dice(self):
        N, M = 2, 7
        self.assertEqual(6, roll_dice(N, M))

        N, M = 3, 9
        self.assertEqual(25, roll_dice(N, M))

        N, M = 8, 24
        self.assertEqual(98813, roll_dice(N, M))