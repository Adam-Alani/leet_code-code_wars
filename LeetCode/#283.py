def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
        nums.append(0)
    return nums

print(moveZeroes([0,0,1]))