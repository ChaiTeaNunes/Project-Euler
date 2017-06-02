# Double-Base Palindromes

def is_palindrome(s):
    if isinstance(s, int):
        s = str(s)
    return s == s[::-1]

def to_base_2(n):
    if isinstance(n, str):
        n = int(n)
    return bin(n)[2:]

def is_double_base_palindrome(n):
    return is_palindrome(n) and is_palindrome(to_base_2(n))

def double_base_palindromes():
    output = list()
    for i in range(1000000):
        if is_double_base_palindrome(i):
            output.append(i)
    return output

print(sum(double_base_palindromes()))
