import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]


"""
DP[i] = 합의 값이 i인 경우의 수
"""

DP = [0] * (K + 1)
DP[0] = 1

for coin in coins:
    for j in range(coin, K + 1):
        DP[j] += DP[j - coin]

print(DP[K])
