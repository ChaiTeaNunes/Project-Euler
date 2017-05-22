# 1000-digit Fibonacci Number

def n_digit_fib(n):
    maximum = pow(10, n-1)
    fib = [0]
    while fib[-1] <= maximum:
        n = len(fib)
        if n == 0: fib.append(0)
        elif n == 1: fib.append(1)
        else: fib.append(fib[n-2]+fib[n-1])
    return len(fib)-1

print(n_digit_fib(1000))
