import sys
read = sys.stdin.readline

N, K = map(int, read().split())
coins = list(dict.fromkeys([int(read()) for _ in range(N)]))

DP = [float('inf')] * (K + 1)
for coin in coins:
    if coin <= K:
        DP[coin] = 1
for i in range(1, K + 1):
    for coin in coins:
        if i > coin:
            DP[i] = min(DP[i], DP[i - coin] + 1)

print(-1 if DP[K] == float('inf') else DP[K])
