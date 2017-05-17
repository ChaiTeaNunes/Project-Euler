# Amicable Numbers

def d(n):
    output = [1]
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            output.append(i)
            output.append(int(n / i))
    return sum(output)

def amicables(start=1, end=10000):
    a = list()
    for i in range(start, end):
        if i == d(d(i)) and i != d(i):
            if not i in a and i < end:
                a.append(i)
            if not d(i) in a and d(i) < end:
                a.append(d(i))
    return a

print(sum(amicables(end=10000)))
