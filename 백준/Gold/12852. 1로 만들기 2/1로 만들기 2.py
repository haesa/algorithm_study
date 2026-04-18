import sys
input = sys.stdin.readline

'''
DP[i]: i를 1로 만드는 연산의 최소 횟수

# i가 3의 배수인 경우
DP[i] = DP[i // 3] + 1

# i가 2의 배수인 경우
DP[i] = DP[i // 2] + 1

# 1을 빼는 경우
DP[i] = DP[i - 1] + 1

이 중 최솟값으로 DP[i]를 업데이트
'''

N = int(input())

DP = [float('inf')] * (N + 1)
DP[1] = 0

path = [-1] * (N + 1)
path[1] = 0

for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1
    path[i] = i - 1

    if i % 3 == 0 and DP[i // 3] + 1 < DP[i]:
        DP[i] = DP[i // 3] + 1
        path[i] = i // 3
    if i % 2 == 0 and DP[i // 2] + 1 < DP[i]:
        DP[i] = DP[i // 2] + 1
        path[i] = i // 2

print(DP[N])
print(N, end=' ')
i = N
while i > 1:
    print(path[i], end=' ')
    i = path[i]
