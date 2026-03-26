import sys
from collections import deque
input = sys.stdin.readline

'''
시작점과 도착점이 N : 1 관계
모든 시작점에 대해 그래프탐색 시도 시 시간초과
도착점에 대해서만 그래프탐색 수행 
'''

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
distance_list = [[-1] * M for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs(r, c):
    q = deque([(r, c, 0)])
    distance_list[r][c] = 0

    while q:
        r, c, d = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if valid_boundary(nr, nc) and board[nr][nc] and distance_list[nr][nc] == -1:
                q.append((nr, nc, d + 1))
                distance_list[nr][nc] = d + 1


def valid_boundary(r, c):
    return r >= 0 and r < N and c >= 0 and c < M


def find_destination():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                return (i, j)


i, j = find_destination()
bfs(i, j)

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance_list[i][j], end=' ')
    print()
