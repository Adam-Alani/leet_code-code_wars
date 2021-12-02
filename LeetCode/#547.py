def dfs(seen, s, cnt, adjlist):
    seen[s] = cnt
    for i in adjlist[s]:
        if seen[i] == 0:
            dfs(seen, i, cnt, adjlist)


def findCircleNum(isConnected):

    n = len(isConnected)
    adjlist = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j] == 1:
                adjlist[i].append(j)
                adjlist[j].append(i)

    seen = [0] * n
    cnt = 1

    for i in range(len(adjlist)):
        if not seen[i]:
            dfs(seen, i, cnt, adjlist)
            cnt += 1
    return cnt - 1


print(findCircleNum([]))
