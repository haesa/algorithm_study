import sys

input = sys.stdin.readline

N, K = map(int, input().split())

DP = [[1] * (N + 1) for _ in range(K + 1)]

for i in range(2, K + 1):
  for j in range(1, N + 1):
    DP[i][j] = (DP[i - 1][j] + DP[i][j - 1]) % 1_000_000_000

print(DP[K][N])
