#Longest Collatz Sequence
collatz = lambda x: x / 2 if x % 2 == 0 else x * 3 + 1

def collatz_length(number=1):
    count = 1
    while number > 1:
        number = collatz(number)
        count += 1
    return count
    
def largest_sequence(maximum):
    num = 0
    largest = 0
    for i in range(0, maximum):
        n = collatz_length(i)
        if (n >= largest):
            largest = n
            num = i
    return num
