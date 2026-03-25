import sys
input = sys.stdin.readline

'''
DP[i] = i번째 잔까지 고려했을 때 포도주의 최대 양
DP[i] = DP[i - 1]   # 안 마시는 경우
DP[i] = wines[i] + DP[i - 2]    # 1잔 건너뛰는 경우
DP[i] = wines[i] + wines[i - 1] + DP[i - 3] # 이어서 마시는 경우
더 큰 경우로 업데이트
'''

N = int(input())
wines = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(wines[1])
elif N == 2:
    print(wines[1] + wines[2])
else:
    DP = [0] * (N + 1)
    DP[1] = wines[1]
    DP[2] = wines[1] + wines[2]
    DP[3] = max(wines[1] + wines[2], wines[2] + wines[3], wines[1] + wines[3])
    for i in range(4, N + 1):
        DP[i] = max(DP[i - 1], wines[i] + DP[i - 2],
                    wines[i] + wines[i - 1] + DP[i - 3])

    print(DP[N])
