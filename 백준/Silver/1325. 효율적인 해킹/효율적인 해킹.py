import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)


def bfs(v):
    q = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1
    count = 1

    while q:
        v = q.popleft()

        for nxt in graph[v]:
            if visited[nxt]:
                continue

            q.append(nxt)
            visited[nxt] = 1
            count += 1
    return count


result = [0] * (N + 1)
for i in range(1, N + 1):
    result[i] = bfs(i)

answer = []
max_count = max(result)
for i, c in enumerate(result):
    if c == max_count:
        answer.append(i)

print(*answer)
