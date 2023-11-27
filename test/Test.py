import circle
import square
import rectangle
import math
import unittest

class RectangleTest(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimetr(self):
        res = rectangle.perimetr(0, 0)
        self.assertEqual(res, 0)


class SquareTest(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = square.area(10000)
        self.assertEqual(res, 100000000)

    def test_zero_perimetr(self):
        res = square.perimetr(0)
        self.assertEqual(res, 0)


class CircleTest(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi)

    def test_zero_perimetr(self):
        res = circle.perimetr(0)
        self.assertEqual(res, 0)
