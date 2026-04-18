import sys

input = sys.stdin.readline

INF = float("inf")

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

"""
DFS 탐색(백트래킹)으로 4칸을 이동하여 테트로미노 도형 방문 체크
'ㅗ' 테트로미노는 날개 4개를 더하고 가장 작은 값을 빼서 계산
"""

# 상 우 하 좌
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[0] * M for _ in range(N)]

result = 0


def dfs(r, c, size, total):
    global result

    if size == 4:
        result = max(total, result)
        return

    for dr, dc in d:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1

            if size == 2:
                dfs(r, c, size + 1, total + board[nr][nc])

            dfs(nr, nc, size + 1, total + board[nr][nc])
            visited[nr][nc] = 0


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0

print(result)
