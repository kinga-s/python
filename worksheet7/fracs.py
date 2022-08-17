# Kinga Syta
# zestaw 7
# 1

"""
W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów
w ułamkach. Dodać możliwości dodawania|odejmowania|mnożenia|dzielenia|porównywania liczb (int, long) do ułamków
(działania lewostronne i prawostronne). Rozważyć możliwość włączenia liczb float do działań na ułamkach.
Napisać kod testujący moduł fracs.
"""

import math


def denominator(n1, n2):
    return (n1 * n2) / math.gcd(n1, n2)


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError("Zero w mianowniku")
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({0}, {1})".format(self.x, self.y)

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        """Sprawdza, czy ułamki są sobie równe"""
        return (self.x * other.y) == (self.y * other.x)

    def __ne__(self, other):
        """Sprawdza, czy ułamki nie są sobie równe"""
        return not (self.x * other.y) == (self.y * other.x)

    def __lt__(self, other):
        """Sprawdza, czy ułamek pierwszy jest mniejszy od drugiego"""
        return (self.x * other.y) < (self.y * other.x)

    def __le__(self, other):
        """Sprawdza, czy ułamek pierwszy jest mniejszy lub równy od drugiego"""
        return (self.x * other.y) <= (self.y * other.x)

    def __gt__(self, other):
        """Sprawdza, czy ułamek pierwszy jest większy od drugiego"""
        return (self.x * other.y) > (self.y * other.x)

    def __ge__(self, other):
        """Sprawdza, czy ułamek pierwszy jest większy lub równy od drugiego"""
        return (self.x * other.y) >= (self.y * other.x)

    def __add__(self, other):  # frac1+frac2, frac+int
        if isinstance(other, Frac):
            x = self.x * other.y + self.y * other.x
            y = self.y * other.y
            return Frac(x, y)
        elif isinstance(other, int):
            x = self.x + other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(other, float):
            x2, y2 = other.as_integer_ratio()
            x = self.x * y2 + self.y * x2
            y = self.y * y2
            return Frac(x, y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, Frac):
            x = self.x * other.y - self.y * other.x
            y = self.y * other.y
            return Frac(x, y)
        elif isinstance(other, int):
            x = self.x - other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(other, float):
            x2, y2 = other.as_integer_ratio()
            x = self.x * y2 - self.y * x2
            y = self.y * y2
            return Frac(x, y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)
        elif isinstance(other, float):
            x2, y2 = other.as_integer_ratio()
            return Frac(self.x * x2, self.y * y2)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other): pass # frac1/frac2, frac/int, Py2

    def __rdiv__(self, other): pass # int/frac, Python 2

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        if isinstance(other, Frac):
            return Frac(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            return Frac(self.x, self.y * other)
        elif isinstance(other, float):
            x2, y2 = other.as_integer_ratio()
            return Frac(self.x * y2, self.y * x2)

    def __rtruediv__(self, other):  # int/frac, Py3
        if isinstance(other, Frac):
            return Frac(other.x * self.y, other.y * self.x)
        elif isinstance(other, int):
            return Frac(self.y * other, self.x)
        elif isinstance(other, float):
            x2, y2 = other.as_integer_ratio()
            return Frac(self.y * x2, self.x * y2)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):   # -frac = (-1)*frac
        return (-1) * self

    def __invert__(self):      # odwrotnosc: ~frac
        return ~self

    def __float__(self):        # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])