# Kinga Syta
# zestaw 7
# 3 testy

import unittest
from rectangles import *


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_rect(self):
        self.assertRaises(ValueError, Rectangle, 4, 3, 2, 1)

    def test_print(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 2, 3, 4).__eq__(Rectangle(1, 2, 3, 4)))

    def test_ne(self):
        self.assertTrue(Rectangle(1, 2, 3, 4).__ne__(Rectangle(1, 2, 3, 5)))

    def test_area(self):
        self.assertEqual(Rectangle(2, 2, 4, 4).area(), 4)

    def test_center(self):
        self.assertEqual(Rectangle(2, 2, 4, 4).center(), Point(3, 3))

    def test_move(self):
        self.assertEqual(Rectangle(2, 2, 4, 4).move(5, 3), Rectangle(7, 5, 9, 7))

    def test_intersection(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).intersection(Rectangle(5, 6, 7, 8)), None)
        self.assertEqual(Rectangle(2, 2, 20, 20).intersection(Rectangle(5, 5, 6, 6)), Rectangle(5, 5, 6, 6))

    def test_cover(self):
        self.assertEqual(Rectangle(2, 2, 4, 4).cover(Rectangle(5, 5, 7, 7)), Rectangle(2, 2, 7, 7))
        self.assertEqual(Rectangle(8, 8, 9, 9).cover(Rectangle(5, 5, 7, 7)), Rectangle(5, 5, 9, 9))

    def test_make4(self):
        self.assertEqual(Rectangle(2, 2, 18, 18).make4(),
            (Rectangle(2, 10, 10, 18), Rectangle(10, 10, 18, 18), Rectangle(10, 2, 18, 10), Rectangle(2, 2, 10, 10)))


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
