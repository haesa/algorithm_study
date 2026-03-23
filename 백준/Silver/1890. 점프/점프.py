import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split()))for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = board[i][j]

        if jump == 0:  # 종착점, 점프 X
            continue
        if i + jump < N:  # 아래로 내려가는 경우
            dp[i + jump][j] += dp[i][j]
        if j + jump < N:  # 오른쪽으로 가는 경우
            dp[i][j + jump] += dp[i][j]


print(dp[N - 1][N - 1])
