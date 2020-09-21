def containsDuplicate(nums):
    if len(set(nums)) < len(nums):
        return True
    return False


print(containsDuplicate([1,2,3,1]))