from collections import defaultdict
def singleNumber(nums):
    hash = defaultdict(int)
    for i in nums:
        hash[i] += 1
    for i in hash:
        if hash[i] == 1:
            return i



    pass



singleNumber([4,1,2,1,2])