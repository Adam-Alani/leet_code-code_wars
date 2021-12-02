def findSmallestSetOfVertices(n, edges):
  s = set(range(n))
  for _,y in edges:
    if y in s:
      s.remove(y)

  #not pythonic bad
  #els = []
  #for el in edges:
    #if el[1] not in els:
      #els.append(el[1])

  #res = []
  #for i in range(n):
    #if i not in els:
      #res.append(i)

  return list(s)

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(findSmallestSetOfVertices(n, edges))
