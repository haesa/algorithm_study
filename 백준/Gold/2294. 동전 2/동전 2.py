import sys
read = sys.stdin.readline

N, K = map(int, read().split())
coins = [int(read().rstrip()) for _ in range(N)]
DP = [float('inf')] * (K + 1)

for coin in reversed(coins):
    if coin <= K:
        DP[coin] = 1
    for i in range(1, K + 1):
        if i - coin > 0 and not DP[i - coin] == float('inf'):
            DP[i] = min(DP[i], DP[i - coin] + 1)

print(-1 if DP[K] == float('inf') else DP[K])