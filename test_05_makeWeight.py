import random
import unittest

from solution import makeWeight


class TestMakeWeight(unittest.TestCase):
    def testEmptySuccess(self):
        self.assertEqual(makeWeight(0, []), [])

    def testEmptyFailure(self):
        self.assertEqual(makeWeight(1, []), None)

    def testTwoFives(self):
        self.assertEqual(makeWeight(10, [7, 5, 4]), None)

    def testTwoFivesFirst(self):
        self.assertEqual(makeWeight(10, [5, 7, 3]), [0, 1, 1])

    def testSevenThree(self):
        self.assertEqual(makeWeight(10, [7, 5, 3]), [1, 0, 1])

    def testFourFives(self):
        self.assertEqual(makeWeight(20, [7, 5, 9]), None)

    def testSevenThreeDoubled(self):
        self.assertEqual(makeWeight(20, [7, 5, 3]), None)

    def testFourFivesFirst(self):
        self.assertEqual(makeWeight(20, [5, 7, 3]), None)

    def testPrimes(self):
        self.assertEqual(makeWeight(20, [11, 13, 17, 19]), None)
        self.assertEqual(makeWeight(21, [11, 13, 17, 19]), None)
        self.assertEqual(makeWeight(23, [11, 13, 17, 19]), None)
