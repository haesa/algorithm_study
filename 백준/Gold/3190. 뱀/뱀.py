import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
directions = deque(
    [tuple(map(lambda x: int(x) if x.isdigit() else x, input().strip().split())) for _ in range(L)]
)

board = [[0] * N for _ in range(N)]  # 0: 빈 칸, 1: 뱀, 2: 사과

board[0][0] = 1  # 뱀의 초기 위치
for r, c in apples:  # 사과 위치 표시
    board[r - 1][c - 1] = 2

# # 상 우 하 좌
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


q = deque([(0, 0)])  # 뱀 몸통의 위치를 저장하는 큐
i = 1  # 초기 방향: 오른쪽
sec = 0
cur_r, cur_c = 0, 0


def turn(i, direct):
    if direct == "L":
        return (i + 3) % 4
    elif direct == "D":
        return (i + 1) % 4


while True:
    sec += 1
    dr, dc = d[i]
    cur_r += dr
    cur_c += dc

    if not (0 <= cur_r < N and 0 <= cur_c < N):
        print(sec)
        break

    if board[cur_r][cur_c] == 1:
        print(sec)
        break

    if board[cur_r][cur_c] == 0:  # 사과가 없는 경우, 꼬리를 제거
        tail_r, tail_c = q.pop()
        board[tail_r][tail_c] = 0

    # 뱀 머리를 새로운 위치로 이동
    q.appendleft((cur_r, cur_c))
    board[cur_r][cur_c] = 1

    if directions and sec == directions[0][0]:
        _, direct = directions.popleft()
        i = turn(i, direct)
