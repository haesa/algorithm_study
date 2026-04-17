import sys
from collections import defaultdict

read = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, read().split())
graph = defaultdict(list)
for _ in range(N - 1):
    v, u, d = map(int, read().split())
    graph[v].append((u, d))
    graph[u].append((v, d))
question = [list(map(int, read().split())) for _ in range(M)]


def dfs(start, end):
    stack = [(start, 0)]
    visited = set([start])

    while stack:
        node, distance = stack.pop()

        if node == end:
            return distance

        for next_node, d in graph[node]:
            if next_node in visited:
                continue
            stack.append((next_node, distance + d))
            visited.add(next_node)


def solution():
    result = []
    for i in range(M):
        start, end = question[i]
        result.append(dfs(start, end))
    write('\n'.join(map(str, result)))


solution()
