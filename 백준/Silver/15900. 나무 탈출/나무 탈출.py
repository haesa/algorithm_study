import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, read().split())
    graph[v].append(u)
    graph[u].append(v)


visited = set([1])


def dfs(node, depth):
    if (node != 1 and len(graph[node]) == 1) or (node == 1 and len(graph[node]) == 0):
        return depth

    total = 0
    for child in graph[node]:
        if child in visited:
            continue
        visited.add(child)
        total += dfs(child, depth + 1)

    return total


write('Yes' if dfs(1,  0) % 2 == 1 else 'No')
