import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

V, E = map(int, read().split())
start = int(read().rstrip())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

dist = [float('inf')] * (V + 1)


def dijkstra(start):
    global dist
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        d, v = heapq.heappop(q)

        for nxt, w in graph[v]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(q, (dist[nxt], nxt))


dijkstra(start)
print(*['INF' if d == float('inf') else d for d in dist[1:]], end='\n')
