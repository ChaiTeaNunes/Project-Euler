#Summation of Primes
import math

def next_prime(n):
    end = math.sqrt(n) + 1
    for mod in range(2, int(end)):
        if n % mod == 0:
            return next_prime(n + 1)
    return n

def prime_list_under_n(n):
    k = 2
    while k < n:
        yield k
        k = next_prime(k + 1)

def prime_sum_under_n(n):
    return sum(prime_list_under_n(n))

print(prime_sum_under_n(2000000))
