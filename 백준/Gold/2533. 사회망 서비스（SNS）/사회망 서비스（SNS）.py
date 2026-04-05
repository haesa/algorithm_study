import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
DP[i][0] = i번 노드가 얼리어답터가 아닌 경우, i번 노드를 루트로하는 서브트리에서 얼리어답터의 최소 수
DP[i][1] = i번 노드가 얼리어답터인 경우, i번 노드를 루트로하는 서브트리에서 얼리어답터의 최소 수
"""

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DP = [[0, 0] for _ in range(N + 1)]

visited = [0] * (N + 1)


def dfs(node):
    visited[node] = 1

    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            DP[node][0] += DP[child][1]
            DP[node][1] += min(DP[child][0], DP[child][1])
    DP[node][1] += 1


dfs(1)
print(min(DP[1][0], DP[1][1]))
