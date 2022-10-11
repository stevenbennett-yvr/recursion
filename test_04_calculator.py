import random
import unittest

from solution import calculator


class TestCalculator(unittest.TestCase):
    def testLegitDigit(self):
        # are legit digits also known as ledigits or legidits?
        # if I told that joke to a French person, they'd call me "le idjit"
        for i in range(0, 9):
            self.assertEqual(calculator(str(i)), i)

    def test5plus5Valid(self):
        self.assertEqual(calculator("(5 + 5)"), 10)

    def testSymmetricAddMult(self):
        self.assertEqual(calculator("((1+1)*(1+1))"), 4)

    def testAllTheOps(self):
        self.assertEqual(calculator("((6 + (2 * (5 - 4))) / 2)"), 4)

    def testAllTheOpsGoesNegative(self):
        self.assertEqual(calculator("((5 + (2 - (5 * 5))) / 2)"), -9)

    def testNegative(self):
        with self.assertRaises(SyntaxError):
            calculator("-1")

    def test5plus5NoParens(self):
        with self.assertRaises(SyntaxError):
            calculator("5 + 5")

    def test5plus5NoOperator(self):
        with self.assertRaises(SyntaxError):
            calculator("( 5 5 )")

    def test5plus5plus5(self):
        with self.assertRaises(SyntaxError):
            calculator("( 5 + 5 + 5 )")

    def testBadOperator(self):
        with self.assertRaises(SyntaxError):
            calculator("( 5 ^ 5 )")
        with self.assertRaises(SyntaxError):
            calculator("( 5 & 5 )")
