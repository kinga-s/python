# Kinga Syta
# zestaw 6
# 2 testy

from points import *
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(-7, -3)), "(-7, -3)")
        self.assertEqual(repr(Point(5, 6)), "Point(5, 6)")
        self.assertEqual(str(Point(60, 99)), "(60, 99)")
        self.assertEqual(repr(Point(0, -8)), "Point(0, -8)")

    def test_eq(self):
        self.assertTrue(Point(5, 5).__eq__(Point(5, 5)))
        self.assertFalse(Point(5, 5).__eq__(Point(5, 6)))

    def test_ne(self):
        self.assertTrue(Point(5, 5).__eq__(Point(5, 6)))
        self.assertFalse(Point(5, 5).__eq__(Point(5, 5)))

    def test_add(self):
        self.assertEqual(Point(3, 4).__add__(Point(5, 5)), Point(8, 9))
        self.assertEqual(Point(7, 7).__add__(Point(-1, 1)), Point(6, 8))

    def test_sub(self):
        self.assertEqual(Point(3, 4).__sub__(Point(5, 5)), Point(-2, -1))
        self.assertEqual(Point(7, 7).__sub__(Point(-1, 1)), Point(8, 6))

    def test_mul(self):
        self.assertEqual(Point(3, 4).__mul__(Point(5, 5)), Point(15, 20))
        self.assertEqual(Point(7, 7).__mul__(Point(-1, 1)), Point(-7, 7))

    def test_cross(self):
        self.assertEqual(Point(1, 1).cross(Point(1, 1)), 0)
        self.assertEqual(Point(2, 3).cross(Point(5, 2)), -11)

    def test_length(self):
        self.assertEqual(Point(6, 8).length(), 10)


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
