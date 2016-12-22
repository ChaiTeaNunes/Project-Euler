# Multiples of 3 and 5
def sum_of_multiples(end, *args):
    sum, counter = 0, 0
    while counter < end:
        for arg in args:
            if i % arg == 0:
                sum += i
                break
        counter += 1
    return sum

print(sum_of_multiples(1000, 3, 5))
