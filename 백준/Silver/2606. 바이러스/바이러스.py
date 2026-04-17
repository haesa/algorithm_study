import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
M = int(read())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph):
    stack = [1]
    visited = set()

    while stack:
        v = stack.pop()

        if v in visited:
            continue
        visited.add(v)

        for next in graph[v]:
            stack.append(next)

    return len(visited) - 1


result = dfs(graph)
write(str(result))
