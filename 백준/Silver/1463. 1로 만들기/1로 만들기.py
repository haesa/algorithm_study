# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys
read = sys.stdin.readline

N = int(read())

DP = [0] * (N + 1)

for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1

    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)


print(DP[N])
