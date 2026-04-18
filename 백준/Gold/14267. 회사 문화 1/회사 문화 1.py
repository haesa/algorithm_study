import sys
read = sys.stdin.readline

N, M = map(int, read().split())
supervisor_list = [0, *list(map(int, read().split()))]  # 상사 리스트

# 직속 상사로부터 받은 칭찬 정도 저장
answer = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, read().split())
    answer[i] += w

for i in range(2, N + 1):
    answer[i] = answer[i] + answer[supervisor_list[i]]

print(*answer[1:])
