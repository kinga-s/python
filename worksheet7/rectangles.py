# Kinga Syta
# zestaw 7
# 3

"""
W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do
obsługi błędów. Napisać kod testujący moduł rectangles.
"""

from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if (not x1 < x2) or (not y1 < y2):
            raise ValueError("Punkty nie spelniaja warunku x1 < x2,  y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta2
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):            # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 > x2 or y1 > y2:
            return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):    # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca krotkę czterech mniejszych
        center = self.center()
        d = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        c = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        b = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        a = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        return (a, b, c, d)

# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C
