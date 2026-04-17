import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
start, end = map(int, read().split())
M = int(read())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, start, end):
    stack = [(start, 0)]
    visited = set()

    while stack:
        v, distance = stack.pop()

        if v in visited:
            continue
        visited.add(v)

        if v == end:
            return distance

        for next in graph[v]:
            stack.append((next, distance + 1))
    return -1


result = dfs(graph, start, end)
write(str(result))
