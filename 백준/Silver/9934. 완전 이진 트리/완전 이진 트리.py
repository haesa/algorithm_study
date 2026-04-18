# 완전 이진 트리가 아니라 포화 이진 트리 문제 같은데? ㅇㅅㅇ
import sys

read = sys.stdin.readline

K = int(read())
inorder = list(map(int, read().split()))
result = [[] for _ in range(K)]


def dfs(graph, k):
    n = len(graph)
    if n < 1:
        return
    mid = n // 2
    result[k].append(graph[mid])

    dfs(graph[:mid], k + 1)
    dfs(graph[mid + 1:], k + 1)


dfs(inorder, 0)
for level in result:
    print(*level)
