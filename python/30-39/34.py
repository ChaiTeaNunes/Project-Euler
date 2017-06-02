# Digit Factorials

def factorial(n):
    output = 1
    for i in range(n):
        output += output * i
    return output

def is_digit_factorial(n):
    digits = [factorial(int(i)) for i in str(n)]
    return sum(digits) == n

def digit_factorials():
    output = list()
    for i in range(10, factorial(9) * 7): # limit
        if is_digit_factorial(i):
            output.append(i)
    return output

print(sum(digit_factorials()))
