import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N, M, V = map(int, read().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited = [0] * (N + 1)
    stack = [v]
    path = []
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        path.append(cur)
        for next in sorted(graph[cur], reverse=True):
            stack.append(next)
    write(' '.join(map(str, path)))


def bfs(v):
    visited = [0] * (N + 1)
    q = deque([v])
    path = []
    while q:
        cur = q.popleft()
        if visited[cur]:
            continue
        visited[cur] = 1
        path.append(cur)
        for next in sorted(graph[cur]):
            q.append(next)
    write(' '.join(map(str, path)))


dfs(V)
write('\n')
bfs(V)
