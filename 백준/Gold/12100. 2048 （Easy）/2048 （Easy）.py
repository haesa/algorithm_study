import copy
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

"""
1. 모든 블럭이 상, 하, 좌, 우 중 한 방향으로 한 번에 이동
2. 같은 숫자가 겹치는 경우, 두 블럭이 합쳐져서 하나의 블럭이 됨
3. 한 번의 이동에서 블럭은 한 번만 합칠 수 있음 (이미 합쳐진 블록을 연속으로 또 합칠 수 없음)
4. 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐짐
5. 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 문제
"""

# 상 하 좌 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move(board, dr, dc):
    if dc == 1:  # 오른쪽으로 이동하는 경우
        for cur_r in range(N):
            nums = board[cur_r]
            stack = []
            for num in reversed(nums):
                if num == 0:
                    continue
                if stack and stack[-1][0] == num:
                    top, is_merged = stack.pop()
                    if is_merged:
                        stack.append((top, is_merged))
                        stack.append((num, 0))
                    else:
                        stack.append((num * 2, 1))
                else:
                    stack.append((num, 0))
            board[cur_r] = [0] * (N - len(stack)) + list(map(lambda x: x[0], reversed(stack)))
    elif dc == -1:  # 왼쪽으로 이동하는 경우
        for cur_r in range(N):
            nums = board[cur_r]
            stack = []
            for num in nums:
                if num == 0:
                    continue
                if stack and stack[-1][0] == num:
                    top, is_merged = stack.pop()
                    if is_merged:
                        stack.append((top, is_merged))
                        stack.append((num, 0))
                    else:
                        stack.append((num * 2, 1))
                else:
                    stack.append((num, 0))

            board[cur_r] = list(map(lambda x: x[0], stack)) + [0] * (N - len(stack))
    elif dr == 1:  # 아래로 이동하는 경우
        for cur_c in range(N):
            nums = [board[cur_r][cur_c] for cur_r in range(N)]
            stack = []
            for num in reversed(nums):
                if num == 0:
                    continue
                if stack and stack[-1][0] == num:
                    top, is_merged = stack.pop()
                    if is_merged:
                        stack.append((top, is_merged))
                        stack.append((num, 0))
                    else:
                        stack.append((num * 2, 1))
                else:
                    stack.append((num, 0))

            for idx, num in enumerate(
                [0] * (N - len(stack)) + list(map(lambda x: x[0], reversed(stack)))
            ):
                board[idx][cur_c] = num

    else:  # 위로 이동하는 경우
        for cur_c in range(N):
            nums = [board[cur_r][cur_c] for cur_r in range(N)]
            stack = []
            for num in nums:
                if num == 0:
                    continue
                if stack and stack[-1][0] == num:
                    top, is_merged = stack.pop()
                    if is_merged:
                        stack.append((top, is_merged))
                        stack.append((num, 0))
                    else:
                        stack.append((num * 2, 1))
                else:
                    stack.append((num, 0))

            for idx, num in enumerate(list(map(lambda x: x[0], stack)) + [0] * (N - len(stack))):
                board[idx][cur_c] = num

    return board


max_block = 0
q = deque([(board, 0)])

while q:
    board, count = q.popleft()

    if count == 5:
        max_block = max(max_block, max(max(row) for row in board))

    if count > 5:
        break

    for dr, dc in direction:
        next_board = move(copy.deepcopy(board), dr, dc)
        q.append((next_board, count + 1))

print(max_block)
