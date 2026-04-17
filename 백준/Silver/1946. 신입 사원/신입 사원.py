import sys

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  scores = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
  scores.sort()
  result = 1
  min_value = scores[0][1]
  for i in range(1, n):
    if min_value >= scores[i][1]: 
      result += 1
      min_value = scores[i][1]
  print(result)