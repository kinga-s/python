# Kinga Syta
# zestaw 8

import random


# 1
"""
Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0. Podać specyfikację problemu. 
Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa. Podać implementację algorytmu w Pythonie 
w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.
"""


def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c != 0:
                print("Równanie nie ma rozwiązań")
            else:
                print("Równanie tożsamościowe")

        else:
            print("Rozwiązaniem równania jest: y =", -c / b)

    elif b == 0:
        print("Rozwiązanie: x =", -c / a)

    else:
        print("Rozwiązanie: y =", -c / b, " +", -a / b, "* x")


solve1(0, 0, 0)
solve1(0, 0, 89)
solve1(0, 99, 0)
solve1(0, 9, 9)
solve1(5, 0, 0)
solve1(5, 0, 7)
solve1(5, 8, 0)
solve1(2, 3, 4)


# 3
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
        n oznacza liczbę losowanych punktów."""
    pi = 0
    square = 0
    circle = 0

    for i in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            circle += 1

        square += 1
        pi = 4.0 * circle / square

    return pi


print("Pi w przybliżeniu wynosi: ", calc_pi())


# 4
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        raise ValueError("Z tych długości nie da się zbudować trójkąta")

    half = (a + b + c) / 2

    return (half * (half - a) * (half - b) * (half - c)) * (1 / 2)


print("Pole trójkąta o bokach 3, 4, 5 wynosi:", heron(3, 4, 5))


# 6
"""
Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0
"""


class PClass:
    def __init__(self):
        self.cache = {(0, 0): 0.5, (1, 0): 0.0, (0, 1): 1.0}

    def __call__(self, i, j):
        if i < 0 | j < 0:
            print("Brak rozwiązań")
            return -1
        if (i, j) in self.cache.keys():
            return self.cache[(i, j)]
        if i == 0:
            return self.cache[(0, 1)]
        if j == 0:
            return self.cache[(1, 0)]
        if i > 0 and j > 0:
            self.cache[(i, j)] = 0.5 * (self(i - 1, j) + self(i, j - 1))
            return self.cache[(i, j)]


def function_p(i, j):
    if i < 0 | j < 0:
        print("Brak rozwiązań")
        return -1

    if i == 0:
        if j == 0:
            return 0.5
        else:
            return 1.0
    elif j == 0:
        return 0.0
    else:
        return 0.5 * (function_p(i - 1, j) + function_p(i, j - 1))


p = PClass()
print("Funkcja p wywołana dynamicznie ", p(18, 6))
print(p.cache)
print("Funkcja p wywołana rekurencyjnie ", function_p(18, 6))
