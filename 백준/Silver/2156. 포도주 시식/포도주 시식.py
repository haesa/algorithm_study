import sys
input = sys.stdin.readline

'''
DP[i] = i번째 잔까지 포도주의 최대양
DP[i] = DP[i - 1] # 안 마시는 경우
DP[i] = wines[i] + wines[i - 1] + DP[i - 3] # 이어서 마시는 경우
DP[i] = wines[i] + DP[i - 2]    # 1잔 건너뛰는 경우
DP[i] = wines[i] + DP[i - 3]    # 2잔 건너뛰는 경우
둘 중 더 큰 경우로 업데이트
'''

N = int(input())
wines = [int(input()) for _ in range(N)]

if N == 1:
    print(wines[0])
elif N == 2:
    print(wines[0] + wines[1])
elif N == 3:
    print(max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2]))
else:
    DP = [0] * N
    DP[0] = wines[0]
    DP[1] = wines[0] + wines[1]
    DP[2] = max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2])

    for i in range(3, N):
        DP[i] = max(DP[i - 1], wines[i] +
                    wines[i - 1] + DP[i - 3], wines[i] + DP[i - 2], wines[i] + DP[i - 3])

    print(max(DP))
