def sortArrayByParity(A):
    res = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            res.append(A[i])
    for i in range(len(A)):
        if A[i] % 2 != 0:
            res.append(A[i])
    return res

print(sortArrayByParity([3,1,2,4]))