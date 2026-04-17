import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1_000_000_000

"""
DP[i][j] = 0 ~ i까지 j개의 수를 골라 i를 만드는 경우의 수

DP[N][K] = DP[N][K - 1] + DP[N - 1][K - 1] + DP[N - 2][K - 1] + ... + DP[0][K - 1]
DP[N - 1][K] = DP[N - 1][K - 1] + DP[N - 2][K - 1] + ... + DP[0][K - 1]
DP[N][K] = DP[N][K - 1] + DP[N - 1][K]
"""

DP = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N + 1):
    DP[i][1] = 1

for i in range(1, K + 1):
    DP[0][i] = 1

for i in range(2, K + 1):
    for j in range(1, N + 1):
        DP[j][i] = (DP[j][i - 1] + DP[j - 1][i]) % MOD

print(DP[N][K])
