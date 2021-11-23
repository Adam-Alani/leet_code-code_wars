def dfs(n,edges,s,end,seen):
    seen[s] = True
    for i in edges[s]:
        if i == end:
            return True
        if not seen[i]:
            if dfs(n,edges,i,end,seen):
                return True
    return False
  
def validPath(n,edges,start,end):
    seen = [False] * n

    if edges == []:
        return True

    adjlist = [[] for _ in range(n)]
    for vertex,edge in edges:
        adjlist[vertex].append(edge)
        adjlist[edge].append(vertex)

    print(adjlist)
    if dfs(n,adjlist,start,end,seen):
        return True
    return False
        
print(validPath(1,[],0,0))