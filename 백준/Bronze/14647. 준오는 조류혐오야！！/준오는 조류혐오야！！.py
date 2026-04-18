n, m = [int(x) for x in input().split(' ')]

bingo = []
for i in range(n):
  bingo.append(input().split(' '))

total_nine = 0
nine_arr = []
for i in range(n):
  str = ''.join(bingo[i])
  count = str.count('9')
  nine_arr.append(count)
  total_nine += count

for j in range(m):
  str = ''
  for i in range(n):
    str += bingo[i][j]
  nine_arr.append(str.count('9'))
  
print(total_nine - max(nine_arr))