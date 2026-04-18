# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.
# 불은 각 지점에서 네 방향으로 확산된다.
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

import sys
from collections import deque
read = sys.stdin.readline

R, C = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(R)]

fire_time = [[R * C] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def is_exit(r, c):
    return r < 0 or r >= R or c < 0 or c >= C


def valid_boudary(r, c):
    return r >= 0 and r < R and c >= 0 and c < C


def fire_dfs(fire_list):
    q = deque([(r, c, 0) for r, c in fire_list])
    for r, c in fire_list:
        fire_time[r][c] = 0

    while q:
        r, c, t = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if valid_boudary(nr, nc) and not graph[nr][nc] == '#' and fire_time[nr][nc] == R * C:
                q.append((nr, nc, t + 1))
                fire_time[nr][nc] = t + 1


def dfs(r, c):
    q = deque([(r, c, 0)])
    visited = [[0] * C for _ in range(R)]
    visited[r][c] = 1

    while q:
        r, c, t = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if is_exit(nr, nc):
                return t + 1
            if not graph[nr][nc] == '#' and not visited[nr][nc] and t + 1 < fire_time[nr][nc]:
                q.append((nr, nc, t + 1))
                visited[nr][nc] = 1
    return -1


start = None
fire_list = []
for r in range(R):
    for c in range(C):
        if graph[r][c] == 'J':
            start = (r, c)
        elif graph[r][c] == 'F':
            fire_list.append((r, c))

fire_dfs(fire_list)
result = dfs(*start)
answer = 'IMPOSSIBLE' if result == -1 else result
print(answer)
