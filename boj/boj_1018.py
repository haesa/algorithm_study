# 입력: M, N (M=행, N=열, W와 B로 이루어진 보드 행렬)
# 로직: 왼쪽 맨상단 칸을 기준으로 한 격자 칸을 board_a, 다른 격자 칸을 board_b라고 하자.
#      완전한 체스판으로 만들기 위해선 board_a와 board_b는 상반 관계여야 한다. (B / W)
#      board_a의 B와 W 개수, board_b의 B와 W 개수를 구한다.
#      board_a를 B라 가정한 경우 board_a의 W와 board_b의 B의 개수를 더한 값이 변경해야할 칸의 개수가 된다.
#      마찬가지로 board_a를 W라고 가정한 경우에 대한 값도 구한다.
#      두 값 중 더 작은 값이 해당 보드판에서 변경해야할 칸의 최솟값이 된다.
#      MN 크기의 보드를 순회하여 8X8 크기의 보드에 대해서 위 과정을 수행하면 문제의 답을 구할 수 있다.
# 출력: 보드를 8X8로 잘라내었을 때 다시 칠해야 하는 정사각형 개수의 최솟값

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
board = []

for _ in range(m):
  board.append(input().strip())

def solve(start_r, start_c):
  # 0번째 인덱스: B, 1번째 인덱스: W
  board_a = [0, 0]
  board_b = [0, 0]
  
  for r in range(8):
    for c in range(8):
      cur_r, cur_c = start_r + r, start_c + c
      
      if (r + c) % 2 == 0:  # board_a에 해당하는 칸
        if board[cur_r][cur_c] == 'B':
          board_a[0] += 1
        else:
          board_a[1] += 1  
      else:   # board_b에 해당하는 칸
        if board[cur_r][cur_c] == 'B':
          board_b[0] += 1
        else:
          board_b[1] += 1
  
  # 해당 보드에서 변경해야할 칸의 개수 최솟값
  return min(board_a[1] + board_b[0], board_a[0] + board_b[1])

result = m * n

# 전체 보드에 대해 최솟값 계산
for r in range(m):
  for c in range(n):
    if (r + 8 <= m) and (c + 8 <= n):
      result = min(result, solve(r, c));
      
print(result)