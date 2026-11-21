'''
DP[k] = 1부터 k까지의 누적합
구간 [i, j]의 부분합 = DP[j] - DP[i - 1]
'''

ans = float('inf')
N, S = map(int, input().split())
arr = list(map(int, input().split()))

DP = [0] * (N + 1)

# DP 누적합 계산
for i in range(1, N + 1):
    DP[i] = DP[i - 1] + arr[i - 1]

s, e = 1, 1
while e <= N and s <= e:
    # 구간합 S 이상이면 최소값 저장 & 구간 시작 오른쪽으로 한 칸 이동 
    if DP[e] - DP[s - 1] >= S:
        ans = min(ans, e - s + 1)
        s += 1
    # 구간합 S 미만이면 구간 끝 오른쪽으로 한 칸 이동
    else:
        e += 1

print(0 if ans == float('inf') else ans)