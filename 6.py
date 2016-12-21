# Sum Square Difference
def square_sum_diff(n=100):
    sum, square_sum, diff = 0, 0, 0
    for i in range(n + 1):
        sum += i**2
        square_sum += i
    square_sum **= 2
    diff = square_sum - sum
    return diff

print(square_sum_diff())
