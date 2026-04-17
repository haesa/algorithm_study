import sys
from collections import deque

read = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(read())

for _ in range(T):
    M, N, K = map(int, read().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, read().split())
        graph[r][c] = 1
    visited = [[0] * M for _ in range(N)]

    def valid_boundary(r, c):
        return r >= 0 and r < N and c >= 0 and c < M

    def bfs(r, c):
        q = deque([(r, c)])
        visited[r][c] = 1

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if valid_boundary(nr, nc) and graph[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if not graph[i][j] or visited[i][j]:
                continue
            bfs(i, j)
            count += 1
    print(count)
