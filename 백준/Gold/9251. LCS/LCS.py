import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

DP = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
  for j in range(1, len(str2) + 1):
    if str1[i - 1] == str2[j - 1]:
      DP[i][j] = DP[i - 1][j - 1] + 1
    else:
      DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

print(DP[len(str1)][len(str2)])