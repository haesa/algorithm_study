import sys
from collections import defaultdict
read = sys.stdin.readline

N, M = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    v1, v2 = map(int, read().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * N
answer = 0


def dfs(v, d):
    global answer
    if answer:
        return
    if d == 4:
        answer = 1
        return

    visited[v] = 1

    if not (v in graph):
        return

    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, d + 1)

    visited[v] = 0


for i in range(N):
    if answer:
        break

    dfs(i, 0)

print(answer)
