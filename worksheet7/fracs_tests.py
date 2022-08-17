# Kinga Syta
# zestaw 7
# 1 testy

import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Frac()

    def test_create_frac(self):
        self.assertRaises(ValueError, Frac, 5, 0)

    def test_print(self):
        self.assertEqual(str(Frac(3, 5)), "3/5")
        self.assertEqual(repr(Frac(3, 5)), "Frac(3, 5)")

    def test_eq(self):
        self.assertTrue(Frac(1, 2).__eq__(Frac(1, 2)))

    def test_ne(self):
        self.assertTrue(Frac(1, 2).__ne__(Frac(1, 5)))

    def test_lt(self):
        self.assertTrue(Frac(1, 2).__lt__(Frac(4, 5)))

    def test_le(self):
        self.assertTrue(Frac(1, 2).__le__(Frac(3, 4)))

    def test_gt(self):
        self.assertTrue(Frac(1, 2).__gt__(Frac(1, 5)))

    def test_ge(self):
        self.assertTrue(Frac(1, 2).__ge__(Frac(1, 4)))

    def test_add(self):
        self.assertEqual(Frac(1, 2).__add__(Frac(1, 4)), Frac(3, 4))
        self.assertEqual(Frac(1, 2).__add__(5), Frac(11, 2))
        self.assertEqual(Frac(1, 2).__add__(5.5), Frac(12, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2).__sub__(Frac(1, 4)), Frac(1, 4))
        self.assertEqual(Frac(11, 2).__sub__(5), Frac(1, 2))
        self.assertEqual(Frac(12, 2).__sub__(5.5), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(1, 2).__mul__(Frac(1, 4)), Frac(1, 8))
        self.assertEqual(Frac(1, 2).__mul__(5), Frac(5, 2))
        self.assertEqual(Frac(1, 2).__mul__(2.5), Frac(5, 4))

    def test_truediv(self):
        self.assertEqual(Frac(1, 2).__truediv__(Frac(1, 4)), Frac(4, 2))
        self.assertEqual(Frac(1, 2).__truediv__(5), Frac(1, 10))
        self.assertEqual(Frac(1, 2).__truediv__(0.5), Frac(2, 2))

    def test_float_frac(self):
        self.assertEqual(float(Frac(8, 9)), 8/9)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
