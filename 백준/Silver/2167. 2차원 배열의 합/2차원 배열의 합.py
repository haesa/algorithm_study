n, m = [int(x) for x in input().split(' ')]

numbers = [0]
for i in range(n):
  numbers += [int(x) for x in input().split(' ')]

dp = [0] * (n * m + 1)

for i in range(1, n * m + 1):
  dp[i] = dp[i - 1] + numbers[i]
  
k = int(input())
start_end = []
for i in range(k):
  start_end.append([int(x) for x in input().split(' ')])

for i in range(k):
  sum = 0
  start_x, start_y, end_x, end_y = start_end[i]
  for j in range(start_x - 1, end_x):
    sum += dp[j * m + end_y] - dp[j * m + start_y - 1]
  print(sum)