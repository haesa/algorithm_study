import sys
read = sys.stdin.readline

N = int(read())
stairs = [int(read()) for _ in range(N)]

DP = [0] * N
DP[0] = stairs[0]
if N >= 2:
    DP[1] = stairs[0] + stairs[1]
if N >= 3:
    DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
for i in range(3, N):
    DP[i] = max(stairs[i] + stairs[i - 1] + DP[i - 3], stairs[i] + DP[i - 2])

print(DP[N - 1])
