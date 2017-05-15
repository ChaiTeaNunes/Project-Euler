# Factorial Digit Sum

def factorial(n):
    output = 1
    for i in range(n):
        output *= (i+1)
    return output
    
def sum_digits(n):
    return sum(map(int, list(str(n))))

print(sum_digits(factorial(100)))
