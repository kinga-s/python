# Kinga Syta
# zestaw 5

# 2
# Ulamki - testy

import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([9, 10], [1, 20]), [17, 20])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([23, 33], [1, 2]), [23, 66])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [7, 8]), [4, 7])

    def test_is_positive(self):
        self.assertEqual(is_positive([26, 99]), True)
        self.assertEqual(is_positive([15, -22]), False)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([-7, -8]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([9, 79]), False)
        self.assertEqual(is_zero([0, 7865]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([21, 22], [22, 23]), -1)
        self.assertEqual(cmp_frac([4, 5], [4, 5]), 0)
        self.assertEqual(cmp_frac([7, 8], [2, 5]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([7, 8]), 7/8)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
