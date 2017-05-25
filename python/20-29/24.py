# Lexicographic Permutations

def perms(n):
    output = 1
    for i in range(n):
        output += output * (i+1)
    return output
            
def nth_perm(n, nums):
    if isinstance(nums, int):
        nums = [i for i in range(nums+1)]
    
    size = len(nums)
    if size == 1:
        return str(nums[0])
    elif size > 1:
        num = int(n / perms(size-2))
        if n % perms(size-2) == 0:
            num -= 1
        digit = nums[num]
        n -= (num * perms(size-2))
        nums.remove(digit)
        return str(digit) + nth_perm(n, nums)
    else:
        return str()

print(nth_perm(1000000, 9))
