import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read())
M = int(read())
graph = defaultdict(list)
for _ in range(M):
    s, e, c = map(int, read().split())
    graph[s].append((e, c))


def floyd_warshall(graph):
    d = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for s in range(1, N + 1):
        for e, w in graph[s]:
            d[s][e] = min(d[s][e], w)
        d[s][s] = 0

    for m in range(1, N + 1):
        for s in range(1, N + 1):
            for e in range(1, N + 1):
                d[s][e] = min(d[s][e], d[s][m] + d[m][e])

    return d


result = floyd_warshall(graph)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(0 if result[i][j] == float('inf') else result[i][j], end=' ')
    print()
