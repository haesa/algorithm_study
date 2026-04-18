import sys
from collections import deque
read = sys.stdin.readline

M, N = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < M


def dfs(start_list):
    q = deque([(r, c, 0) for r, c in start_list])
    result = 0

    while q:
        r, c, d = q.popleft()
        result = d
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if valid_boundary(nr, nc) and not visited[nr][nc]:
                q.append((nr, nc, d + 1))
                visited[nr][nc] = 1

    if any(0 in row for row in visited):
        return -1

    return result


start_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start_list.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == -1:
            visited[i][j] = 1

print(dfs(start_list))
