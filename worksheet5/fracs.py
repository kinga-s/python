# Kinga Syta
# zestaw 5

# 2
# Ułamki
'''
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch
liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction
z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
'''

import math


def denominator(n1, n2):
    return (n1 * n2) / math.gcd(n1, n2)


def add_frac(frac1, frac2):
    counter = frac1[0] * (denominator(frac1[1], frac2[1]) / frac1[1]) + frac2[0] * (denominator(frac1[1], frac2[1]) / frac2[1])
    return [counter, denominator(frac1[1], frac2[1])]


def sub_frac(frac1, frac2):
    counter = frac1[0] * (denominator(frac1[1], frac2[1]) / frac1[1]) - frac2[0] * (denominator(frac1[1], frac2[1]) / frac2[1])
    return [counter, denominator(frac1[1], frac2[1])]


def mul_frac(frac1, frac2):
    counter = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return [counter / math.gcd(counter, den), den / math.gcd(counter, den)]


def div_frac(frac1, frac2):
    return mul_frac(frac1, frac2[::-1])


def is_positive(frac):
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    a1 = frac1[0] * (denominator(frac1[1], frac2[1]) / frac1[1])
    a2 = frac2[0] * (denominator(frac1[1], frac2[1]) / frac2[1])

    if a1 > a2:
        return 1
    elif a1 == a2:
        return 0
    else:
        return -1


def frac2float(frac):
    return frac[0] / frac[1]
