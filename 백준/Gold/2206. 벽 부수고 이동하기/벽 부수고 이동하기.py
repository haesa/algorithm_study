import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [list(map(int, read().rstrip())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < M


def bfs():
    if N == 1 and M == 1:
        return 1

    q = deque([(0, 0, 1, 0)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while q:
        r, c, t, f = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not valid_boundary(nr, nc):
                continue

            if nr == N - 1 and nc == M - 1:
                return t + 1

            if graph[nr][nc] == 0 and not visited[nr][nc][f]:
                q.append((nr, nc, t + 1, f))
                visited[nr][nc][f] = 1
            elif graph[nr][nc] == 1 and f == 0 and not visited[nr][nc][1]:
                q.append((nr, nc, t + 1, 1))
                visited[nr][nc][1] = 1

    return -1


print(bfs())
