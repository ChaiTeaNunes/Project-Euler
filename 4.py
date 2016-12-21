# Largest Palindrome Product
def largest_palindrome(digits=3):
    start, end = 10**(digits - 1), 10**digits
    value, output = 0, 0
    
    for i in range(start, end):
        for j in range(i, end):
            value = i * j
            temp = str()
            for k in range(len(str(value)) - 1, -1, -1):
                temp += str(value)[k]
            if temp == str(value) and value >= output:
                output = value
            del temp
    return output

largest_palindrome()
