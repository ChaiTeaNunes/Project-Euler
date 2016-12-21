# Largest Palindrome Product
def largest_palindrome():
    start, end = 100, 1000
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
    print(output)

largest_palindrome()
