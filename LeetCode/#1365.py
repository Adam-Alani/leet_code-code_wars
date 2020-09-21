def smallerNumbersThanCurrent(nums):
    res = []
    c = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                c += 1
        res.append(c)
        c = 0
    return res



print(smallerNumbersThanCurrent([8,1,2,2,3]))