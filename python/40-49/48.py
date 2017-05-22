# Self Powers

def series(size):
    output = 0
    for i in range(1, size+1):
        output += pow(i, i)
    return output

print(series(1000) % pow(10, 10))
