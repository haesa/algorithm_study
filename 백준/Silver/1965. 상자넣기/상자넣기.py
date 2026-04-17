import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
