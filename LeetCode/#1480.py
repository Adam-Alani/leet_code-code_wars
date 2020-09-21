def runningSum(nums):
    i = 0
    for j in range(1, len(nums)):
        nums[j] = nums[i] + nums[j]
        i += 1
    return nums


print(runningSum([3,1,2,10,1]))