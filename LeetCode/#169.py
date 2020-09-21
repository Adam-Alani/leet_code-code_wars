def majorityElement(nums):
    return max(set(nums), key = nums.count)


print(majorityElement([3,2,3]))