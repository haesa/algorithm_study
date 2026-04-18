import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    if 1 <= N <= 3:
        print(1)
    elif 4 <= N <= 5:
        print(2)
    else:
        DP = [0] * (N + 1)
        DP[1] = DP[2] = DP[3] = 1
        DP[4] = DP[5] = 2
        for i in range(6, N + 1):
            DP[i] = DP[i - 1] + DP[i - 5]
        print(DP[N])
