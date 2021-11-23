

class Solution:
    def cycle(self,seen, adjlist, s, prerequisites):

        # seen[s] has been visited, cycle
        if seen[s] == 1:
            return True

        # seen[s] has not been visited, no cycle
        if seen[s] == 0:
            return False

        seen[s] = 1
        for i in adjlist[s]:
            if self.cycle(self,seen, adjlist, i, prerequisites):
                return True
        seen[s] = 0

        # no cycle found
        return False

    def getAdjlist(self,n, prerequisites):
        adjlist = [[] for _ in range(n)]

        for a1, a2 in prerequisites:
            adjlist[a2].append(a1)
        return adjlist

    def canFinish(self,numCourses, prerequisites):
        adjlist = self.getAdjlist(numCourses, prerequisites)
        seen = [-1] * numCourses

        for i in range(numCourses):
            if self.cycle(self,seen, adjlist, i, prerequisites):
                return False
        return True


s = Solution
print(s.canFinish(s,2, [[1, 0], [0, 1]]))
