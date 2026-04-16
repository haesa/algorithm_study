import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]


"""
1. bfs로 크기가 4 이상인 서브 그래프 탐색 (빨, 초, 파, 보, 노)
2. 뿌요뿌요 빈 공간으로 드롭
"""

# 상 우 하 좌
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(sr, sc, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    colors = set([(sr, sc)])
    color = board[sr][sc]

    while q:
        r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 12 and 0 <= nc < 6 and board[nr][nc] == color and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                colors.add((nr, nc))

    return colors


def drop():
    new_board = [[0] * 12 for _ in range(6)]

    # 시계 방향 회전
    for i in range(12):
        for j in range(6):
            new_board[j][11 - i] = board[i][j]

    # 왼쪽으로 시프트
    for i in range(6):
        new_board[i] = [x for x in new_board[i] if x != "."] + ["."] * new_board[i].count(".")

    # 반시계 방향 회전
    for i in range(6):
        for j in range(12):
            board[11 - j][i] = new_board[i][j]


count = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    flag = False

    for i in range(12):
        for j in range(6):
            if board[i][j] == "." or visited[i][j]:
                continue

            colors = bfs(i, j, visited)

            if len(colors) >= 4:
                flag = True
                for r, c in colors:  # 터짐 처리
                    board[r][c] = "."

    if flag:
        count += 1
    else:
        break

    drop()

print(count)
