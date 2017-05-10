#Lattice Paths

def paths(size=1):
    pascal = [[1] * (size + 1)]
    for i in range(1, size + 1):
        temp = [1]
        for j in range(1, size + 1):
            temp.append(temp[j-1] + pascal[i-1][j])
        pascal.append(temp)
    return pascal[-1][-1]

print(paths(20))
