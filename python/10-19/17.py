# Number Letter Counts

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
unique = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 15:"fifteen", 18:"eighteen",
    20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 80:"eighty"}

def ones_and_tens(n):
    output = str()
    if n > 0:
        if n in unique.keys():
            return unique[n]
        elif n < 10:
            return digits[n - 1]
        elif n < 100:
            ones_place = n % 10
            tens_place = n - ones_place
            
            if n < 20:
                return digits[ones_place - 1] + "teen"
            else:
                if tens_place in unique.keys():
                    output += unique[tens_place]
                else:
                    output += digits[int(tens_place / 10) - 1] + "ty"
                    
                if ones_place > 0:
                    output += digits[ones_place - 1]
    return output

def hundreds(n):
    output = str()
    if n > 0:
        if n < 100:
            return ones_and_tens(n)
        elif n < 1000:
            hundreds_place = n - (n % 100)
            output += digits[int(hundreds_place / 100) - 1] + "hundred"
            if ones_and_tens(n % 100) != str():
                output += "and" + ones_and_tens(n % 100)
    return output

def thousands(n):
    output = str()
    if n > 0:
        if n < 1000:
            return hundreds(n)
        elif n < 10000:
            thousands_place = n - (n % 1000)
            output += digits[int(thousands_place / 1000) - 1] + "thousand"
            if hundreds(n % 1000) != str():
                output += hundreds(n % 1000)
    return output

def num_letters(n):
    return len(thousands(n))

def letter_counts(end=1000):
    output = 0
    for i in range(1, end+1):
        output += num_letters(i)
    return output
        
print(letter_counts(1000))
