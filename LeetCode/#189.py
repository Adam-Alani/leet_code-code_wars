def rotate(nums,k):
    j = 1
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k],nums[-k:]
    k -= 1
    return nums


print(rotate([-1,-100,3,99],2))