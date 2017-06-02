# Non-Abundant Sums

LIMIT = 28123 # Predefined upper limit by mathematical analysis

def d(n):
    output = [1]
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            output.append(i)
            if i*i != n:
                output.append(int(n / i))
    return sum(output)

def abundants():
    output = list()
    for i in range(2, LIMIT+1):
        if d(i) > i:
            output.append(i)
    return output

def abundant_sums():
    output = [False] * (LIMIT+1)
    nums = abundants()
    for i in nums:
        for j in nums:
            if i + j <= LIMIT:
                output[i+j] = True
    return output

def non_abundant_sum():
    output = 0
    sums = abundant_sums()
    for i, is_sum in enumerate(sums):
        if not is_sum:
            output += i
    return output

print(non_abundant_sum())
