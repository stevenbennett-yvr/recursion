import random
import unittest

from solution import makeWeightMulti


class TestMakeWeightMulti(unittest.TestCase):
    def testEmptySuccess(self):
        self.assertEqual(makeWeightMulti(0, []), [])

    def testEmptyFailure(self):
        self.assertEqual(makeWeightMulti(1, []), None)

    def testTwoFives(self):
        self.assertEqual(makeWeightMulti(10, [7, 5, 4]), [0, 2, 0])

    def testTwoFivesFirst(self):
        self.assertEqual(makeWeightMulti(10, [5, 7, 3]), [2, 0, 0])

    def testSevenThree(self):
        self.assertEqual(makeWeightMulti(10, [7, 5, 3]), [1, 0, 1])

    def testFourFives(self):
        self.assertEqual(makeWeightMulti(20, [7, 5, 9]), [0, 4, 0])

    def testSevenThreeDoubled(self):
        self.assertEqual(makeWeightMulti(20, [7, 5, 3]), [2, 0, 2])

    def testFourFivesFirst(self):
        self.assertEqual(makeWeightMulti(20, [5, 7, 3]), [4, 0, 0])

    def testPrimes(self):
        self.assertEqual(makeWeightMulti(20, [11, 13, 17, 19]), None)
        self.assertEqual(makeWeightMulti(21, [11, 13, 17, 19]), None)
        self.assertEqual(makeWeightMulti(23, [11, 13, 17, 19]), None)
