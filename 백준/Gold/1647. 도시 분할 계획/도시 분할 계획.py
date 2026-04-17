import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

N, M = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, read().split())
    graph[A].append((B, C))
    graph[B].append((A, C))


def prim(graph, start):
    q = [(0, start)]
    visited = [0] * (N + 1)
    total = 0
    max_c = 0
    while q:
        c, v = heapq.heappop(q)
        if visited[v]:
            continue
        visited[v] = 1
        total += c
        max_c = c if c > max_c else max_c

        for nxt, w in graph[v]:
            if not visited[nxt]:
                heapq.heappush(q, (w, nxt))

    return total - max_c


print(prim(graph, 1))
