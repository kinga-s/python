# Kinga Syta
# zestaw 6
# 2
'''
W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione
w początku układu współrzędnych, o końcu w położeniu (x, y). Napisać kod testujący moduł points.
'''

import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        """konstuktor"""
        self.x = x
        self.y = y

    def __str__(self):
        """zwraca string "(x, y)" """
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        """zwraca string "Point(x, y)" """
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        """obsługa point1 == point2"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """obsługa point1 != point2"""
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        """v1 + v2"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """v1 * v2, iloczyn skalarny, zwraca liczbę"""
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):
        """v1 x v2, iloczyn wektorowy 2D, zwraca liczbę"""
        return self.x * other.y - self.y * other.x

    def length(self):
        """długość wektora"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points
