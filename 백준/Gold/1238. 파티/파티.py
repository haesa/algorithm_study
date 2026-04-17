import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

N, M, X = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    u, v, t = map(int, read().split())
    graph[u].append((v, t))

dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for s in range(1, N + 1):
    for e, t in graph[s]:
        dist[s][e] = t
    dist[s][s] = 0


def solution(start):
    global dist
    q = []
    for i, _ in graph[start]:
        heapq.heappush(q, (dist[start][i], i))

    while q:
        d, v = heapq.heappop(q)
        if d > dist[start][v]:
            continue

        for nxt, t in graph[v]:
            if dist[start][v] + t < dist[start][nxt]:
                dist[start][nxt] = dist[start][v] + t
                heapq.heappush(q, (dist[start][nxt], nxt))


for i in range(1, N + 1):
    solution(i)

result = []
for i in range(1, N + 1):
    result.append(dist[i][X] + dist[X][i])
print(max(result))
