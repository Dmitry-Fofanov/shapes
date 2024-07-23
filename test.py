import math
import unittest

import shapes


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        radius = 2
        circle = shapes.Circle(radius)
        self.assertAlmostEqual(circle.get_area(), math.pi * radius ** 2)

    def test_triangle_area(self):
        triangle = shapes.Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0)

    def test_is_right_triangle(self):
        triangle = shapes.Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_not_right_triangle(self):
        triangle = shapes.Triangle(4, 4, 5)
        self.assertFalse(triangle.is_right_triangle())


if __name__ == '__main__':
    unittest.main()
