# Number Spiral Diagonals

def diagonal_sums(size):
    output = [1]
    for i in range(1, int(size/2)+1):
        for _ in range(0, 4):
            output.append(output[-1] + i*2)
    return sum(output)

print(diagonal_sums(1001))
