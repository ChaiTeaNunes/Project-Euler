# Maximum Path Sum II

def parse(triangle_file):
    unparsed = open(triangle_file)
    parsed = unparsed.read().split('\n')
    parsed = [[int(i) for i in s.split(' ') if i != ''] for s in parsed]
    return parsed

def largest_adjacent(triangle, row=0, index=0):
    a, b = triangle[row][index], triangle[row][index+1]
    if a > b:
        return a
    return b
        
def fix_triangle_row(triangle, row):
    for i in range(len(triangle[row])):
        triangle[row][i] += largest_adjacent(triangle, row+1, i)
    return triangle[row]

def largest_sum(triangle):
    size = len(triangle)-1
    for i in range(size):
        triangle[size-i] = fix_triangle_row(triangle, size-i-1)
    return triangle[0][0]

tri100 = parse("67.txt")
print(largest_sum(tri100))
