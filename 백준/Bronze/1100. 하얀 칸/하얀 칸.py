white_board = []
for i in range(8):
  str = list(input())
  if i % 2 == 0:
    white_board += [str[i] for i in range(8) if i % 2 == 0]
  else:
    white_board += [str[i] for i in range(8) if i % 2 != 0]

result = 0
for c in white_board:
  if c == 'F':
    result += 1
    
print(result)