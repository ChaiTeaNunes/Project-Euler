# Even Fibonacci Numbers
MAX = 4000000
prev_fib = 1
current_fib = 1
next_fib = 0
sum = 0

while (sum <= MAX):
    next_fib = current_fib + prev_fib
    if next_fib % 2 == 0:
       sum += next_fib
    prev_fib = current_fib
    current_fib = next_fib

print(sum)
