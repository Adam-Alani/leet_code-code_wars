def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j +=1
            nums[i] = nums[j]
    return j+1



print(removeDuplicates([1,1,2]))