import sys
from collections import deque

read = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, read().split())
jump = {}

for _ in range(N + M):
    start, end = map(int, read().split())
    jump[start] = end

board = [0] * 101
dice = [1, 2, 3, 4, 5, 6]


def dfs():
    q = deque([(1, 0)])
    board[1] = 1

    while q:
        pos, count = q.popleft()
        if pos == 100:
            return count

        for dice_num in dice:
            next_pos = pos + dice_num
            next_pos = jump[next_pos] if next_pos in jump else next_pos
            if next_pos > 100 or board[next_pos]:
                continue
            q.append((next_pos, count + 1))
            board[next_pos] = 1


write(str(dfs()))
