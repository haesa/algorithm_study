# ---------------------------------------------------------------------------------------------------------------------------
#  문제
# ---------------------------------------------------------------------------------------------------------------------------
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.


import sys
from collections import deque

read = sys.stdin.readline


d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def valid_boundary(r, c, W, H):
    return r >= 0 and r < H and c >= 0 and c < W


def bfs(r, c, W, H, graph, visited):
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for offset_r, offset_c in d:
            nxt_r = r + offset_r
            nxt_c = c + offset_c

            if valid_boundary(nxt_r, nxt_c, W, H) and graph[nxt_r][nxt_c] and not visited[nxt_r][nxt_c]:
                q.append((nxt_r, nxt_c))
                visited[nxt_r][nxt_c] = 1


while True:
    W, H = map(int, read().split())
    if not W and not H:
        break
    graph = [list(map(int, read().split())) for _ in range(H)]

    count = 0
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j, W, H, graph, visited)
                count += 1

    print(count)
