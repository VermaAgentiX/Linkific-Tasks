def missing_number(nums):
    n = len(nums)
    exp = n * (n + 1) // 2
    act = sum(nums)
    return exp - act


print(missing_number([3, 0, 1]))