# Kinga Syta
# zestaw 6
# 1 testy

from times import *
import unittest


class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(3723)
        self.t2 = Time(3603)
        self.t3 = Time(7500)

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(self.t1), "01:02:03")
        self.assertEqual(repr(self.t1), "Time(3723)")
        self.assertEqual(str(self.t2), "01:00:03")
        self.assertEqual(repr(self.t2), "Time(3603)")
        self.assertEqual(str(self.t3), "02:05:00")
        self.assertEqual(repr(self.t3), "Time(7500)")


    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

        self.assertTrue(Time(8) == Time(8))
        self.assertFalse(Time(9) == Time(4))
        self.assertTrue(Time(88) != Time(25))
        self.assertFalse(Time(5) != Time(5))
        self.assertTrue(Time(10) < Time(12))
        self.assertFalse(Time(44) < Time(33))
        self.assertTrue(Time(7) <= Time(50))
        self.assertFalse(Time(9) <= Time(8))
        self.assertTrue(Time(9) > Time(7))
        self.assertFalse(Time(21) > Time(31))
        self.assertTrue(Time(15) >= Time(15))
        self.assertFalse(Time(5) >= Time(26))


    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(5) + Time(6), Time(11))
        self.assertEqual(Time(60) + Time(25), Time(85))
        self.assertEqual(Time(1).__add__(Time(2)), Time(3))
        self.assertEqual(Time(5).__add__(Time(6)), Time(11))
        self.assertEqual(Time(60).__add__(Time(25)), Time(85))

    def test_int(self):
        self.assertEqual(int(Time(1234)), 1234)
        self.assertEqual(int(Time(8888)), 8888)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

