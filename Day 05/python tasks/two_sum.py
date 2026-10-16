def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        comp = target - num

        if comp in seen:
            return [seen[comp], i]

        seen[num] = i

    return []


print(two_sum([2, 7, 11, 15], 9))