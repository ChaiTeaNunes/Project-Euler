#Special Pythagorean Triplet
def is_triplet(a, b, c):
    return a**2 + b**2 == c**2

def triplet_sum(a, b, c):
    if is_triplet(a, b, c):
        return a + b + c
