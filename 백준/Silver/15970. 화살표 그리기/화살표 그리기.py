n = int(input())

spot = []
for i in range(n):
  spot.append([int(x) for x in input().split(' ')])

sorted_spot = sorted(spot, key = lambda x: (x[1], x[0]))

MAX = 10**5
result = 0
for i in range(len(sorted_spot)):
  left = MAX
  right = MAX
  if i > 0 and sorted_spot[i][1] == sorted_spot[i - 1][1]:
    left = sorted_spot[i][0] - sorted_spot[i - 1][0]
  if i < len(sorted_spot) - 1 and sorted_spot[i][1] == sorted_spot[i + 1][1]:
    right = sorted_spot[i + 1][0] - sorted_spot[i][0]
  result += min(left, right)
  
print(result)