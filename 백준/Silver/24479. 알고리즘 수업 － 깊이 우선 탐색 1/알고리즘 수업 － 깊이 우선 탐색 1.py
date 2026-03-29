import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E, R = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, V + 1):
    graph[i].sort()

result = [0] * (V + 1)
order = 1


def dfs(v):
    global order
    result[v] = order

    for u in graph[v]:
        if result[u] == 0:
            order += 1
            dfs(u)


dfs(R)
for i in range(1, V + 1):
    print(result[i])
