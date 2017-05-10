# Power Digit Sum

def sum_str(num):
    nums = [int(s) for s in num]
    return sum(nums)

def power_digit_sum(base, power):
    num = str(pow(base, power))
    return sum_str(num)

print(power_digit_sum(2, 1000))
