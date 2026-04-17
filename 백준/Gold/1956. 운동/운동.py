import sys
from collections import defaultdict
read = sys.stdin.readline

V, E = map(int, read().split())
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, read().split())
    graph[A].append((B, C))


def floyd_warshall(graph):
    dist = [[float('inf')] * (V + 1) for _ in range(V + 1)]
    for s in range(1, V + 1):
        for e, w in graph[s]:
            dist[s][e] = w
        dist[s][s] = 0

    for m in range(1, V + 1):
        for s in range(1, V + 1):
            for e in range(1, V + 1):
                dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])
    return dist


answer = float('inf')
dist = floyd_warshall(graph)
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            continue
        answer = min(answer, dist[i][j] + dist[j][i])
print(-1 if answer == float('inf') else answer)
