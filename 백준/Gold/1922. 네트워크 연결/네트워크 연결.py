import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

N = int(read())
M = int(read())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def prim(graph, start):
    q = [(0, start)]
    visited = [0] * (N + 1)
    result = 0

    while q:
        c, v = heapq.heappop(q)
        if visited[v]:
            continue
        result += c
        visited[v] = 1

        for nxt, w in graph[v]:
            if not visited[nxt]:
                heapq.heappush(q, (w, nxt))

    return result


print(prim(graph, 1))
