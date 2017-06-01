# Distinct Powers

def distinct_powers(start, end):
    output = list()
    for a in range(start, end+1):
        for b in range(start, end+1):
            output.append(a**b)
    output = list(set(output))
    output.sort()
    return output

print(len(distinct_powers(2, 100)))
