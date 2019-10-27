# Multiples of 3 and 5
def multiples(x, y, n):
    result = 0
    for i in range(n):
        if i % x != 0 and i % y != 0:
            result += i
    return result


print(multiples(3, 5, 1000))
