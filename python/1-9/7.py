# 10001st prime
import math

def next_prime(n):
    end = math.sqrt(n) + 1
    for mod in range(2, int(end)):
        if n % mod == 0:
            return next_prime(n + 1)
    return n

def get_prime_list(n):
    count = 1
    prime = 2
    prime_list = list()
    while count <= n:
        prime_list.append(next_prime(prime))
        prime = next_prime(prime) + 1
        count += 1
    return prime_list

def nth_prime(n):
    return get_prime_list(n)[-1]

print(nth_prime(10001))
