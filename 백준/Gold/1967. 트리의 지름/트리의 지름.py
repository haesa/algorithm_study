import sys
from collections import deque, defaultdict

read = sys.stdin.readline

N = int(read())
graph = defaultdict(list)
for _ in range(N - 1):
    parent, child, weight = map(int, read().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))


def bfs(start):
    q = deque([start])
    distance = [-1] * (N + 1)
    distance[start] = 0

    while q:
        node = q.popleft()

        for nxt, w in graph[node]:
            if distance[nxt] == -1:
                q.append(nxt)
                distance[nxt] = distance[node] + w

    max_distance = max(distance)
    index = distance.index(max_distance)
    return max_distance, index


_, index = bfs(1)
distance, _ = bfs(index)
print(distance)
