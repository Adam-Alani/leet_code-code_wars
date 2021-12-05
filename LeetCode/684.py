def dfs(seen,s,edges):
    seen[s] = True
    for i in edges[s]:
        if not seen[i]:
            dfs(seen,i,edges)
            
def findRedundantConnection(edges):
    seen = [False] * len(edges)

    for i in range(len(edges)):
        if not seen[i]:
            dfs(seen,i,edges)

    return seen

print(findRedundantConnection([[1,2],[1,3],[2,3]]))