# TODO
def path(start, end):


def eventualSafeNodes(graph):
    res = []
    for i in range(len(graph)):
        if graph[i] == []:
            res.append(i)

    for i in range(len(graph)):
        if i in res:
            continue
        if all(x in res for x in graph[i]):
            res.append(i)

    return sorted(res)


graph = [[], [0, 2, 3, 4], [3], [4], []]

print(eventualSafeNodes(graph))
