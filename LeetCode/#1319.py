class Solution:
    def components(self, seen, cnt, s, adjlist):
        seen[s] = cnt

        for i in adjlist[s]:
            if seen[i] == 0:
                self.components(seen, cnt, i, adjlist)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        adjlist = [[] for _ in range(n)]
        for el in connections:
            adjlist[el[0]].append(el[1])
            adjlist[el[1]].append(el[0])

        seen = [0] * n
        count = 0
        for i in range(n):
            if seen[i] == 0:
                count += 1
                self.components(seen, count, i, adjlist)

        return count - 1
