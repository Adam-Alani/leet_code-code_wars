def dailyTemperatures(T):
    res = [0 for _ in range(len(T))]
    stack = []
    for i, temps in enumerate(T):
        while stack and temps > stack[-1][1]:
            j, t2 = stack.pop()
            res[j] = i - j
        stack.append((i, temps))
    return res
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))