n, m = [int(x) for x in input().split(' ')]

paint = []
for i in range(n):
  paint.append(input())
    
result = [[0] * n for _ in range(m)]

for i in range(n):
  for j in range(m):
    if paint[i][j] == '-':
      result[m - 1 - j][i] = '|'
    elif paint[i][j] == '|':
      result[m - 1 - j][i] = '-'
    elif paint[i][j] == '/':
      result[m - 1 - j][i] = '\\'
    elif paint[i][j] == '\\':
      result[m - 1 - j][i] = '/'
    elif paint[i][j] == '^':
      result[m - 1 - j][i] = '<'
    elif paint[i][j] == '<':
      result[m - 1 - j][i] = 'v'
    elif paint[i][j] == 'v':
      result[m - 1 - j][i] = '>'
    elif paint[i][j] == '>':
      result[m - 1 - j][i] = '^'
    else:
      result[m - 1 - j][i] = paint[i][j]

for x in result:
  print(''.join(x))