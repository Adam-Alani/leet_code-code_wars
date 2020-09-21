def maxSubArray(nums):
    final = cur = nums[0]
    for i in range(1,len(nums)):
        cur = max(cur + nums[i], nums[i])
        final = max(cur, final)
    return final



print(maxSubArray([1]))




