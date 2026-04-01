import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A = [0] + A

"""
DP[i] = i번째 수를 기준으로 하는 가장 긴 바이토닉 부분 수열의 길이
DP_UP[i] = i번째 수를 기준으로 하는 가장 긴 증가하는 부분 수열의 길이
DP_DOWN[i] = i번째 수를 기준으로 하는 가장 긴 감소하는 부분 수열
DP[i] = DP_UP[i] + DP_DOWN[i] - 1
"""

DP_UP = [1] * (N + 1)
DP_DOWN = [1] * (N + 1)
DP = [1] * (N + 1)

# 증가하는 부분 수열
for i in range(2, N + 1):
    for j in range(1, i):
        if A[i] > A[j]:
            DP_UP[i] = max(DP_UP[i], DP_UP[j] + 1)

# 감소하는 부분 수열
for i in range(N - 1, 0, -1):
    for j in range(N, i, -1):
        if A[i] > A[j]:
            DP_DOWN[i] = max(DP_DOWN[i], DP_DOWN[j] + 1)


# 바이토닉 부분 수열
for k in range(1, N + 1):
    DP[k] = DP_UP[k] + DP_DOWN[k] - 1

print(max(DP))
