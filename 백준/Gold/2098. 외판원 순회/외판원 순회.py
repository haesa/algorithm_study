import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

"""
1. 모든 도시 방문 후 출발점으로 되돌아와야함
2. 사이클을 찾는 문제
3. 출발점 고정 후 DFS로 탐색

DP[현재 도시][방문 상태] = 앞으로 남은 모든 도시를 다 돌고 출발점으로 돌아가기 위해 필요한 "최소 비용"
* 방문 상태 = 지금까지 방문한 노드 집합, 비트마스킹으로 구현
"""

DP = [[-1] * (2**N) for _ in range(N)]


def dfs(i, visited):
    if visited == 2**N - 1:  # 모든 도시 방문한 경우
        return W[i][0] if W[i][0] > 0 else float("inf")

    if DP[i][visited] != -1:
        return DP[i][visited]

    DP[i][visited] = float("inf")

    for j, w in enumerate(W[i]):
        if w == 0:  # 길이 없는 경우
            continue
        if visited & (1 << j) > 0:  # 이미 방문한 경우
            continue

        DP[i][visited] = min(dfs(j, visited | (1 << j)) + W[i][j], DP[i][visited])

    return DP[i][visited]


print(dfs(0, 1 << 0))
