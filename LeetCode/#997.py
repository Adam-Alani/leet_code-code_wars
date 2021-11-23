class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:    
        adjlist = [[] for _ in range(n)]
        for el in trust:
            adjlist[el[0]-1].append(el[1]-1)
        l = len(adjlist)
        found = True
        for i in range(l):
            if adjlist[i] == []:
                for j in range(l):
                    if j != i:
                        if i not in adjlist[j]:
                            found = False
                            break
                if found:
                    return i+1
                found = True

        return -1
       