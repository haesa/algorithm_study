n = int(input())
cmds = input()

# initialize board
board = [[0] * 100 for _ in range(100)]
start_position = 50
board[start_position][start_position] = 1

# initialize direction
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북, 동, 남, 서

direction_idx = 2
current_r = current_c = start_position
for cmd in cmds:
  if cmd == 'L':
     direction_idx = (direction_idx + 3) % 4
  elif cmd == 'R':
    direction_idx = (direction_idx + 1) % 4
  elif cmd == 'F':
    dr, dc = direction[direction_idx]
    current_r += dr
    current_c += dc
    board[current_r][current_c] = 1

min_r = min_c = 100
max_r = max_c = 0
for r in range(100):
  for c in range(100):
    if board[r][c] == 1:
      min_r = min(min_r, r)
      max_r = max(max_r, r)
      min_c = min(min_c, c)
      max_c = max(max_c, c)
  
for r in range(min_r, max_r + 1):
  for c in range(min_c, max_c + 1):
    if board[r][c] == 1:
      print('.', end = '')
    else:
      print('#', end = '')
  print()