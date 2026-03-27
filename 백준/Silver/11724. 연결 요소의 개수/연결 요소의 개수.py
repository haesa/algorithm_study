import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        v = q.popleft()

        for u in graph[v]:
            if not visited[u]:
                q.append(u)
                visited[u] = 1


count = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
