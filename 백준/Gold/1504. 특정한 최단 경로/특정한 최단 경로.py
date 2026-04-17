import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

N, E = map(int, read().split())
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, read().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
V1, V2 = map(int, read().split())


def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, v = heapq.heappop(q)
        if d > dist[v]:
            continue

        for nxt, w in graph[v]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(q, (dist[nxt], nxt))
    return dist


dist_1 = dijkstra(1)
dist_v1 = dijkstra(V1)
dist_v2 = dijkstra(V2)

answer = min(dist_1[V1] + dist_v1[V2] + dist_v2[N],
             dist_1[V2] + dist_v2[V1] + dist_v1[N])
print(-1 if answer == float('inf') else answer)
