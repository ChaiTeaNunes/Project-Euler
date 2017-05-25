# Lexicographic Permutations

def perms(n):
    output = 1
    for i in range(0, n):
        output += output * (i+1)
    return output

def nth_perm(n, nums):
    if isinstance(nums, int):
        nums = [i for i in range(nums+1)]
        
    size = len(nums)-1
    if size <= 0:
        return str(nums[0])
    for i, num in enumerate(nums):
        if n <= (i+1) * perms(size-1):
            n -= i * perms(size-1)
            nums.remove(num)
            return str(num) + nth_perm(n, nums)
    
    return str(nums[0])

print(nth_perm(1000000, 9))
