def dfs(seen,s, rooms):
  seen[s] = True

  for i in rooms[s]:
    if not seen[i]:
      dfs(seen,i,rooms)

def canVisitAllRooms(rooms):
  seen = [False] * len(rooms)

  dfs(seen,0, rooms)
  return all(seen)

print(canVisitAllRooms( [[1],[2],[3],[]]))


# 0