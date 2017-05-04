#Highly Divisible Triangle Number
from functools import reduce

def num_factors(n=1):
    return len(set(reduce(list.__add__, \
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def get_triangle_numbers(factors=1):
    i = 1
    num = i
    while 1:
        if (num_factors(num) > factors):
            break
        i += 1
        num += i
    return num

print(get_triangle_numbers(500))
