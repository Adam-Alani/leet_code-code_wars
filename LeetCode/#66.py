def plusOne(digits):
    res = 0
    for i in range(len(digits)):
        res += (digits[i]* pow(10, len(digits)-1-i))
    return [int(i) for i in str(res+1)]


print(plusOne([1,2,3]))