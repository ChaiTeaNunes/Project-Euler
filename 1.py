# Multiples of 3 and 5
sum = 0

def is_of_3(n):
    if n % 3 == 0:
        return True
    return False

def is_of_5(n):
    if n % 5 == 0:
        return True
    return False
    
for i in range(0, 1000):
    if is_of_3(i) or is_of_5(i):
        sum += i

print(sum)
