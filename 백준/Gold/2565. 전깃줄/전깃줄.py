import sys

input = sys.stdin.readline
input = sys.stdin.readline

N = int(input())

"""
DP[i] = i번째 전선을 포함하는 가장 긴 증가하는 부분 수열의 길이
"""

lines = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
lines = [[0, 0]] + lines

DP = [1] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i):
        if lines[i][1] > lines[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))
