import sys
import heapq
from collections import defaultdict
read = sys.stdin.readline

V, E = map(int, read().split())
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, read().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

visited = [0] * (V + 1)


def solution(start):
    q = [(0, start)]
    result = 0

    while q:
        w, v = heapq.heappop(q)
        if visited[v]:
            continue

        result += w
        visited[v] = 1

        for nxt, c in graph[v]:
            if not visited[nxt]:
                heapq.heappush(q, (c, nxt))

    return result


print(solution(1))
