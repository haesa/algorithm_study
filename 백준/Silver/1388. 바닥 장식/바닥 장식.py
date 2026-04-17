import sys
import math

read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(read())

visited = [[0] * M for _ in range(N)]


def check_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < M


def solution(r, c):
    stack = [(r, c)]
    visited[r][c] = 1
    target = graph[r][c]

    while stack:
        r, c = stack.pop()

        nxt_r = r if graph[r][c] == '-' else r + 1
        nxt_c = c if graph[r][c] == '|' else c + 1

        if check_boundary(nxt_r, nxt_c) and graph[nxt_r][nxt_c] == target and not visited[nxt_r][nxt_c]:
            stack.append((nxt_r, nxt_c))
            visited[nxt_r][nxt_c] = 1


answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            solution(i, j)
            answer += 1
print(answer)
