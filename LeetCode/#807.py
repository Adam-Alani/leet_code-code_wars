def maxIncreaseKeepingSkyline(grid):
    top = [max(t) for t in zip(*grid)]
    left = [max(l) for l in grid]
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            diff = min(top[j], left[i]) - grid[i][j]
            res += diff
    return res

print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))

# ---// OLD //---

# [[3, 0, 8, 4],
#  [2, 4, 5, 7],
#  [9, 2, 6, 3],
#  [0, 3, 1, 0] ]

# ---// NEW //---

# [[8, 4, 8, 7],
#  [7, 4, 7, 7],
#  [9, 4, 8, 7],
#  [3, 3, 3, 3] ]
