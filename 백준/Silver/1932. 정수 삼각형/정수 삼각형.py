import sys
read = sys.stdin.readline

N = int(read())
triangle = [list(map(int, read().split())) for _ in range(N)]

DP = [[0] * i for i in range(1, N + 1)]
DP[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            DP[i][j] = DP[i - 1][j] + triangle[i][j]
        elif j == i:
            DP[i][j] = DP[i - 1][j - 1] + triangle[i][j]
        else:
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + triangle[i][j]

print(max(DP[N - 1]))
