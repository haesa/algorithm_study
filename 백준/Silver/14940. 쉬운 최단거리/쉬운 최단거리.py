import sys
from collections import deque

input = sys.stdin.readline

"""
시작점과 도착점이 N : 1 관계
모든 시작점에 대해 그래프탐색 시도 시 시간초과
도착점에 대해서만 그래프탐색 수행 
"""

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def solution(r, c):
    q = deque([(r, c)])
    dist[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):  # 유효한 인덱스인지 확인
                continue
            if board[nr][nc] and dist[nr][nc] == -1:  # 갈 수 있고, 아직 방문하지 않은 노드인 경우
                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1

    for d in dist:
        print(*d)


r, c = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:  # 0인 곳 초기화
            dist[i][j] = 0
        elif board[i][j] == 2:  # 시작점
            r, c = i, j

solution(r, c)
