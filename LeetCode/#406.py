def reconstructQueue(people):
    res = []
    for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
        res.insert(k, [h,k])
    print(res)
    return res




reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])