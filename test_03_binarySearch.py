import random
import unittest

from solution import binarySearch


class TestBinarySearch(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(binarySearch([], random.random()), None)
        self.assertEqual(binarySearch([], random.random()), None)
        self.assertEqual(binarySearch([], random.random()), None)

    def testSingleYes(self):
        x = random.random()
        self.assertEqual(binarySearch([x], x), 0)

    def testSingleTooBig(self):
        x = random.random()
        self.assertEqual(binarySearch([x], x + 1), None)

    def testSingleTooSmall(self):
        x = random.random()
        self.assertEqual(binarySearch([x], x - 1), None)


    def testTenTooSmallSlightly(self):
        arr = sorted(random.sample(range(10, 100), 10))
        self.assertEqual(binarySearch(arr, arr[0] - 1), None)

    def testTenTooSmallLots(self):
        arr = sorted(random.sample(range(10, 100), 10))
        self.assertEqual(binarySearch(arr, arr[0] - arr[-4]), None)

    def testTenTooLargeSlightly(self):
        arr = sorted(random.sample(range(10, 100), 10))
        self.assertEqual(binarySearch(arr, arr[-1] + 1), None)

    def testTenTooLargeLots(self):
        arr = random.sample(range(10, 100), 10)
        self.assertEqual(binarySearch(arr, arr[-1] * 2), None)

    def testTenAllTheHits(self):
        arr = sorted(random.sample(range(10, 100), 10))
        for i, element in enumerate(arr):
            self.assertEqual(binarySearch(arr, element), i)

    def testTenAllTheNearMisses(self):
        arr = [i * 2 for i in sorted(random.sample(range(10, 100), 10))]
        for i, element in enumerate(arr):
            self.assertEqual(binarySearch(arr, element - 1), None)
            self.assertEqual(binarySearch(arr, element + 1), None)
    
    def testDuplicatesFoundIt(self):
        arr = [5, 7, 7, 7, 7, 7, 10]
        self.assertIn(binarySearch(arr, 5), [0])
        self.assertIn(binarySearch(arr, 7), [1, 2, 3, 4, 5])
        self.assertIn(binarySearch(arr, 10), [6])

        
    def testDuplicatesNope(self):
        arr = [5, 7, 7, 7, 7, 7, 10]
        self.assertEqual(binarySearch(arr, 4), None)
        self.assertEqual(binarySearch(arr, 6), None)
        self.assertEqual(binarySearch(arr, 9), None)
        self.assertEqual(binarySearch(arr, 11), None)
