import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# 상 하 좌 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = set()  # (red_r, red_c, blue_r, blue_c) 형태로 방문 여부 체크

# 빨간 구슬과 파란 구슬의 초기 위치 찾기
red_r, red_c = 0, 0
blue_r, blue_c = 0, 0

for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            red_r, red_c = r, c
        elif board[r][c] == "B":
            blue_r, blue_c = r, c


def bfs(red_sr, red_sc, blue_sr, blue_sc):
    q = deque([(red_sr, red_sc, blue_sr, blue_sc, 0)])
    visited.add((red_sr, red_sc, blue_sr, blue_sc))

    while q:
        red_r, red_c, blue_r, blue_c, count = q.popleft()

        if count >= 10:
            return -1

        for dr, dc in direction:
            red_nr, red_nc, red_dist = roll(red_r, red_c, dr, dc)
            blue_nr, blue_nc, blue_dist = roll(blue_r, blue_c, dr, dc)

            if (
                board[red_nr][red_nc] == "O" and board[blue_nr][blue_nc] == "O"
            ):  # 동시에 빠지는 경우
                continue

            if board[blue_nr][blue_nc] == "O":  # 파란 구슬이 빠지는 경우
                continue

            if board[red_nr][red_nc] == "O":  # 빨간 구슬이 빠지는 경우
                return count + 1

            if red_nr == blue_nr and red_nc == blue_nc:  # 빨간 구슬과 파란 구슬이 겹치는 경우
                if red_dist > blue_dist:  # 빨간 구슬이 더 멀리 이동한 경우
                    red_nr -= dr
                    red_nc -= dc
                else:  # 파란 구슬이 더 멀리 이동한 경우
                    blue_nr -= dr
                    blue_nc -= dc

            if (red_nr, red_nc, blue_nr, blue_nc) not in visited:
                q.append((red_nr, red_nc, blue_nr, blue_nc, count + 1))
                visited.add((red_nr, red_nc, blue_nr, blue_nc))

    return -1


def roll(r, c, dr, dc):
    dist = 0
    while board[r][c] != "#" and board[r][c] != "O":
        r += dr
        c += dc
        dist += 1

    if board[r][c] == "O":
        return r, c, dist

    if board[r][c] == "#":
        return r - dr, c - dc, dist - 1


print(bfs(red_r, red_c, blue_r, blue_c))
