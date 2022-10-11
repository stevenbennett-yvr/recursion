import unittest

from solution import sumNested


class TestSumNested(unittest.TestCase):
    def test_scalar_01(self):
        self.assertEqual(sumNested(2), 2)

    def test_scalar_02(self):
        self.assertEqual(sumNested(-2), -2)

    def test_single_01(self):
        self.assertEqual(sumNested([2]), 2)

    def test_single_02(self):
        self.assertEqual(sumNested([-2]), -2)

    def test_triple_01(self):
        self.assertEqual(sumNested([17, 0, 222]), 239)

    def test_triple_02(self):
        self.assertEqual(sumNested([-2, -1, 1]), -2)

    def test_nested(self):
        self.assertEqual(sumNested([[1]]), 1)

    def test_complicated(self):
        self.assertEqual(sumNested([[1], [], [-3, [2, 2]]]), 2)
