import sys

input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

"""
DFS 탐색(백트래킹)으로 4칸을 이동하여 테트로미노 도형 방문 체크
산모양 테트로미노는 중간에서 분기하는 형태이므로 별도 계산
"""

# 상 우 하 좌
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[0] * M for _ in range(N)]


def dfs(r, c, size):
    if size == 4:
        return board[r][c]

    visited[r][c] = 1
    max_value = 0

    for dr, dc in d:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            max_value = max(max_value, dfs(nr, nc, size + 1))

    visited[r][c] = 0

    return max_value + board[r][c]


def calc(r, c):
    max_value = 0

    for i in range(4):
        value = board[r][c]

        nr, nc = r + d[i][0], c + d[i][1]
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        value += board[nr][nc]

        # 분기
        base_r, base_c = nr, nc
        for di in [-1, 1]:
            ni = (i + di + 4) % 4
            nr = base_r + d[ni][0]
            nc = base_c + d[ni][1]

            if not (0 <= nr < N and 0 <= nc < M):
                break

            value += board[nr][nc]

        max_value = max(value, max_value)

    return max_value


result = 0
for i in range(N):
    for j in range(M):
        result = max(result, dfs(i, j, 1))
        result = max(result, calc(i, j))

print(result)
