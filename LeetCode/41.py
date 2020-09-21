def firstMissingPositive(nums):
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i] = len(nums) + 1
    for i in range(len(nums)):
        if abs(nums[i]) <= len(nums):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
    for i in range(len(nums)):
        return i+1
    pass

print(firstMissingPositive([1,2,0]))
