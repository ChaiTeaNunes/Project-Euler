#Lattice Paths

def paths(size=1):
	output = [1] * (size + 1)
	for i in range(size):
		for j in range(size):
			output[j+1] = output[j] + output[j+1]
	return output[-1]

print(paths(20))
