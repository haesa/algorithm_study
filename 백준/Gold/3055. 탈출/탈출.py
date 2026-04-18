# 사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
# 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.
# 티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.
# 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
# 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
# 티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

import sys
from collections import deque
read = sys.stdin.readline

INF = float('inf')

R, C = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

water_time = [[INF] * C for _ in range(R)]


def valid_boundary(r, c):
    return r >= 0 and r < R and c >= 0 and c < C


def bfs_water(water_list, end_r, end_c):
    q = deque([(r, c, 0) for r, c in water_list])
    for r, c in water_list:
        water_time[r][c] = 0

    while q:
        r, c, t = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr == end_r and nc == end_c:
                continue

            if valid_boundary(nr, nc) and not graph[nr][nc] == 'X' and water_time[nr][nc] == INF:
                q.append((nr, nc, t + 1))
                water_time[nr][nc] = t + 1


def bfs(start_r, start_c, end_r, end_c):
    q = deque([(start_r, start_c, 0)])
    visited = [[0] * C for _ in range(R)]
    visited[start_r][start_c] = 1

    while q:
        r, c, t = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr == end_r and nc == end_c:
                return t + 1

            if valid_boundary(nr, nc) and graph[nr][nc] == '.' and not visited[nr][nc] and t + 1 < water_time[nr][nc]:
                q.append((nr, nc, t + 1))
                visited[nr][nc] = 1
    return -1


water_list = []
start = None
end = None
for r in range(R):
    for c in range(C):
        if graph[r][c] == '*':
            water_list.append((r, c))
        elif graph[r][c] == 'S':
            start = (r, c)
        elif graph[r][c] == 'D':
            end = (r, c)

bfs_water(water_list, *end)
result = bfs(*start, *end)
print(result if result > -1 else 'KAKTUS')
