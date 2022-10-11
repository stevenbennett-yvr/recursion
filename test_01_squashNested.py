import unittest

from solution import squashNested


class TestSquashNested(unittest.TestCase):
    def test_scalar_01(self):
        self.assertEqual(squashNested(2), [2])

    def test_single_01(self):
        self.assertEqual(squashNested([2]), [2])

    def test_single_02(self):
        self.assertEqual(squashNested([-2]), [-2])

    def test_triple_01(self):
        self.assertEqual(squashNested([17, 0, 222]), [17, 0, 222])

    def test_nested(self):
        self.assertEqual(squashNested([[1]]), [1])

    def test_very_nested(self):
        self.assertEqual(squashNested([[[[[1]]]]]), [1])

    def test_complicated_01(self):
        self.assertEqual(squashNested([[5, 4], [3, [[2]], 1]]), [5, 4, 3, 2, 1])

    def test_complicated_02(self):
        self.assertEqual(squashNested([[1], [], [-3, [2, 2]]]), [1, -3, 2, 2])
