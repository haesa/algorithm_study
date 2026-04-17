import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

N = int(read())
M = int(read())
graph = defaultdict(list)
for _ in range(M):
    s, e, w = map(int, read().split())
    graph[s].append((e, w))
S, E = map(int, read().split())


def dijkstra(graph, s, e):
    dist = [float('inf')] * (N + 1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        d, v = heapq.heappop(q)
        if d > dist[v]:
            continue

        for nxt, w in graph[v]:
            if d + w < dist[nxt]:
                dist[nxt] = dist[v] + w
                heapq.heappush(q, (dist[nxt], nxt))
    return dist


result = dijkstra(graph, S, E)
print(result[E])
