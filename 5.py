# Smallest Multiple
def smallest_multiple():
    output = 20
    while not (output % 20 == 0 and output % 19 == 0 and \
        output % 17 == 0 and output % 16 == 0 and \
        output % 13 == 0 and output % 11 == 0 and \
        output % 9 == 0 and output % 7 == 0):
            output += 20
    return output

print(smallest_multiple())
