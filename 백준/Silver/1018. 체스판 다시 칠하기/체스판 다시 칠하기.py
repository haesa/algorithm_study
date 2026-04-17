# 입력: M, N (M=행, N=열, W와 B로 이루어진 보드 행렬)
# 로직:
# 출력: 보드를 8X8로 잘라내었을 때 다시 칠해야 하는 정사각형 개수의 최솟값

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
board = []

for _ in range(m):
  board.append(input().strip())
    
def solve(start_r, start_c):
  board_a = [0, 0]
  board_b = [0, 0]
  
  for r in range(8):
    for c in range(8):
      cur_r, cur_c = start_r + r, start_c + c
      
      if (r + c) % 2 == 0:
        if board[cur_r][cur_c] == 'B':
          board_a[0] += 1
        else:
          board_a[1] += 1  
      else:
        if board[cur_r][cur_c] == 'B':
          board_b[0] += 1
        else:
          board_b[1] += 1

  return min(board_a[1] + board_b[0], board_a[0] + board_b[1])

result = m * n

for r in range(m):
  for c in range(n):
    if (r + 8 <= m) and (c + 8 <= n):
      result = min(result, solve(r, c));
      
print(result)