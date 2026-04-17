import sys
read = sys.stdin.readline

N = int(read())
A = []
for _ in range(N):
    A.append(int(read()))

DP = [0] * N

if N == 1:
    print(A[0])
elif N == 2:
    print(A[0] + A[1])
else:
    DP[0] = A[0]
    DP[1] = A[0] + A[1]
    DP[2] = max(A[0] + A[1], A[1] + A[2], A[0] + A[2])
    for i in range(3, N):
        DP[i] = max(DP[i - 1], A[i] + DP[i - 2], A[i] + A[i - 1] + DP[i - 3])

    print(DP[N - 1])
