# Kinga Syta
# zestaw 4

# 2
'''
Napisać program rysujący "miarkę" o zadanej długości. Należy zbudować pełny string, a potem go wypisać.
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
'''


def make_ruler(n):
    """Make a ruler"""
    ruler = '| '
    m = 10
    for x in range(n):
        ruler += '. . . . | '
    ruler += '\n0'
    for x in range(n):
        helper = str(x + 1)
        ruler += ''.ljust(m - len(helper), ' ') + helper
    return ruler


print(make_ruler(3))


def make_grid(rows, cols):
    """Make a grid"""
    grid = ''
    for x in range(rows * 2 + 1):
        if x % 2 == 0:
            grid += '+'
            for y in range(cols):
                grid += '---+'
            grid += '\n'
        else:
            grid += '|'
            for y in range(cols):
                grid += '   |'
            grid += '\n'
    return grid


print(make_grid(3, 4))

# 3
'''
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
'''

def factorial(n):
    """Calculating factorial - iterative version"""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print('9! is', factorial(9))

# 4
'''
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
'''


def fibonacci(n):
    """Fibonacci sequence - iterative version"""
    a = 0
    b = 1
    total = 0
    if n < 0:
        print('Number should not be negative.')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n):
            total = a + b
            a = b
            b = total
        return total


print('The 24th Fibonacci number is', fibonacci(24))

# 5
'''
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
'''


def reverse1(L, left, right):
    """Reverse the list - iterative version """
    in_range = int((right - left) / 2) + 1
    for x in range(in_range):
        L[left + x], L[right - x] = L[right - x], L[left + x]


def reverse2(L, left, right):
    """Reverse the list - recursive version """
    if left >= right:
        return L
    else:
        L[left], L[right] = L[right], L[left]
        return reverse2(L, left+1, right-1)


normal_list = []
normal_list += [x for x in range(100)]
reverse1((normal_list), 20, 60)
print(normal_list)

reverse2(normal_list, 15, 25)
print(normal_list)

# 6
'''
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone 
podsekwencje.
'''


def sum_seq(sequence):
    """Calculate the sum of the sequence"""
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total


sequence = [[234, 75, 43, 24, 5, 3, [34, 45]], 45, 34, [45, 0], (1, 2)]
print('Sequence sum is', sum_seq(sequence))


# 7
'''
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się 
nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich 
elementów sekwencji.
'''
total = []


def flatten(sequence, total):
    """Flatten the sequence"""
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatten(item, total)
        else:
            total += [item]
    return total


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print('Flatten sequence', flatten(seq, total))
