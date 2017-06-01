# Digit Fifth Powers

def is_power_sum(n):
    digits = [int(i)**5 for i in list(str(n))]
    return sum(digits) == n

def digit_fifth_powers():
    output = list()
    for i in range(2, 1000000):
        if is_power_sum(i):
            output.append(i)
    return output

print(sum(digit_fifth_powers()))
