import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N, M, K, X = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, read().split())
    graph[A].append(B)


def bfs(graph, start, k):
    q = deque([(start, 0)])
    visited = [0] * (N + 1)
    visited[start] = 1
    result = []

    while q:
        v, d = q.popleft()
        if d == k:
            result.append(v)

        for nxt in graph[v]:
            if not visited[nxt]:
                q.append((nxt, d + 1))
                visited[nxt] = 1

    return result


answer = bfs(graph, X, K)
print(*sorted(answer) if len(answer) else [-1], sep='\n')
