import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# 상 하 좌 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1

    melt_count = 0

    while q:
        r, c = q.popleft()

        if board[r][c]:  # 치즈인 경우
            board[r][c] = 0
            melt_count += 1
            continue

        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return melt_count


time = 0
count = 0

while True:
    melt_count = bfs(0, 0)

    if melt_count == 0:
        break

    time += 1
    count = melt_count

print(time)
print(count)
