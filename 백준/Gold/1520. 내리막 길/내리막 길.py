import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]

"""
DP[i][j] = (i, j)에서 (M-1, N-1)로 가는 경로의 수
"""

# 상 하 좌 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 미방문 표시는 -1
DP = [[-1] * N for _ in range(M)]
DP[M - 1][N - 1] = 1


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1

    if DP[r][c] >= 0:
        return DP[r][c]

    count = 0
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < M and 0 <= nc < N):
            continue
        if board[nr][nc] < board[r][c]:
            count += dfs(nr, nc)
    DP[r][c] = count
    return DP[r][c]


dfs(0, 0)
print(DP[0][0])
