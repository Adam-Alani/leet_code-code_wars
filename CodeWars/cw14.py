import numpy as np
def snail(snail_map):
    arr = []
    m = np.array(snail_map, int)
    while len(m) > 0:
        arr.extend(m[0])
        m = np.delete(m, (0), axis=0)
        m = np.rot90(m)
    return(arr)



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print((snail(array)))