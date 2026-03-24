import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < M


def bfs(r, c):
    q = deque([(r, c, 1)])
    visited[r][c] = 1

    while q:
        r, c, d = q.popleft()

        if r == N - 1 and c == M - 1:
            return d

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if valid_boundary(nr, nc) and maze[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc, d + 1))
                visited[nr][nc] = 1


print(bfs(0, 0))
