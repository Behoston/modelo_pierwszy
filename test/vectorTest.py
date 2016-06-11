# coding=utf8
import unittest

from domain.Vector import Vector


class VectorTest(unittest.TestCase):
    def test_construct_zero_vector(self):
        v = Vector()
        self.assertEqual(v.dim, 0)
        self.assertEqual(v.v, [])

    def test_construct(self):
        coordinates = [1, 2, -3.3, 0]
        v = Vector(coordinates)
        self.assertEqual(v.dim, 4)
        self.assertEqual(v.v, coordinates)

    def test_length(self):
        v = Vector([0, 5])
        self.assertEqual(v.length(), 5)

    def test_multiple_by_vector(self):
        v1 = Vector([2, 2])
        v2 = Vector([3, 3])
        result = v1 * v2
        self.assertEqual(result, 12)

    def test_multiple_by_number_left(self):
        v = Vector([2.6, 25])
        result = 2 * v
        self.assertEqual(result, Vector([5.2, 50]))

    def test_multiple_by_number(self):
        v = Vector([2, 25])
        result = v * 2
        self.assertEqual(result, Vector([4, 50]))

    def test_multiple_is_side_stable(self):
        v = Vector([2, 6, 5, 52, 8, 58])
        n = 8.5
        self.assertEqual(n * v, v * n)

    def test_subtract_vector(self):
        v1 = Vector([2, 2])
        v2 = Vector([1, -15])
        result = v1 - v2
        self.assertEqual(result, Vector([1, 17]))

    def test_subtract_number(self):
        v = Vector([5, 6, 7, 8])
        result = v - 3.1
        self.assertEqual(result, Vector([1.9, 2.9, 3.9, 4.9]))

    def test_divide(self):
        v = Vector([5, 6])
        result = v / 2
        self.assertEqual(result, Vector([2.5, 3]))


if __name__ == '__main__':
    unittest.main()
