import sys
input = sys.stdin.readline
MOD = 1_000_000_000

'''
끝자리가 0으로 끝나는 경우, 이전 단계 계단수 중 1로 끝나는 수에 0을 붙인다
DP[i][0] = DP[i - 1][1]

9로 끝나는 경우, 이전 단계 계단수 중 8로 끝나는 수에 9를 붙인다
DP[i][9] = DP[i - 1][8]

1~8로 끝나는 경우, 이전 단계 계단수 중 k - 1, k + 1로 끝나는 수에 k를 붙인다
DP[i][k] = DP[i - 1][k - 1] + DP[i - 1][k + 1]
'''

N = int(input())

DP = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    DP[1][i] = 1

for i in range(2, N + 1):
    DP[i][0] = DP[i - 1][1]
    DP[i][9] = DP[i - 1][8]
    for k in range(1, 9):
        DP[i][k] = (DP[i - 1][k - 1] + DP[i - 1][k + 1]) % MOD

print(sum(DP[N]) % MOD)
