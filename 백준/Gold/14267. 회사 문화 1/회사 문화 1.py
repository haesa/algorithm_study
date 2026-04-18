import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N, M = map(int, read().split())
supervisor_list = [0, *list(map(int, read().split()))]  # 상사 리스트

# 상사 - 부하 매핑
sub_dict = defaultdict(list)
for i in range(1, N + 1):
    sub_dict[supervisor_list[i]].append(i)

# 직속 상사로부터 받은 칭찬 정도 저장
answer = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, read().split())
    answer[i] += w


def bfs():
    q = deque([1])  # 사장부터 시작

    while q:
        i = q.popleft()

        for sub in sub_dict[i]:  # 부하 직원 탐색
            q.append(sub)
            answer[sub] = answer[sub] + answer[i]  # 칭찬 정도 누적합


bfs()
print(*answer[1:])
