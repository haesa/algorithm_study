import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

"""
상, 하, 좌, 우 중 한 방향으로 한 번에 이동
  => (보드를 시계 방향 90도로 회전한 후 왼쪽으로 이동) * 4

블럭이 이동할 때, 같은 수가 있는 블럭끼리 합쳐짐
  => 스택을 이용해서 구현
"""

# 상 하 좌 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move_left(board):
    new_board = [[] for _ in range(N)]

    for i, row in enumerate(board):
        stack = []
        for num in row:
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

        new_board[i] = list(map(lambda x: x[0], stack)) + [0] * (N - len(stack))

    return new_board


def rotate(board):
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[j][N - 1 - i] = board[i][j]

    return new_board


result = 0


def dfs(board, count):
    global result
    result = max(result, max(map(max, board)))

    if count == 5:
        return

    for _ in range(4):
        dfs(move_left(board), count + 1)
        board = rotate(board)


dfs(board, 0)
print(result)
