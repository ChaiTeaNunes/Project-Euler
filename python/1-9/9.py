#Special Pythagorean Triplet
import math

def is_triple(a, b, c):
    return a**2 + b**2 == c**2

def triple_sum(a, b, c):
    if is_triple(a, b, c):
        return a + b + c
    else:
        return -1

def find_triple_sum(n):
    for c in range(1, n - 3): # a could be 1 but no less and b could be 2 but no less
        for b in range(1, n - c):
            a = n - b - c
            if a > b:
                a, b = b, a
            if triple_sum(a, b, c) == n:
                return [a, b, c]

def triple_product(n):
    triple_list = find_triple_sum(n)
    result = 1
    if triple_list is not None:
        for i in triple_list:
            result *= i
        return result
    return -1

print(triple_product(1000))
