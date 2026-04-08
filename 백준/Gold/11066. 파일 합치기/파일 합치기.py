import sys

input = sys.stdin.readline

"""
DP[i][j] = i번째 파일부터 j번째 파일을 하나로 합치는 데 필요한 최소 비용
"""

T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))

    DP = [[0] * (K + 1) for _ in range(K + 1)]

    cost = [0] * (K + 1)
    for i in range(1, K + 1):
        cost[i] = cost[i - 1] + files[i]

    for length in range(2, K + 1):
        for i in range(1, K - length + 2):
            j = i + length - 1
            DP[i][j] = float("inf")
            merge_cost = cost[j] - cost[i - 1]
            for k in range(i, j):
                DP[i][j] = min(DP[i][k] + DP[k + 1][j] + merge_cost, DP[i][j])

    print(DP[1][K])
